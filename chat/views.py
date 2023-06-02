from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import Chat
from .serializers import GetMessageSerializer, SendMessageSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_messages(request):
    item = Chat.objects.all().order_by('send_time')
    serializer = GetMessageSerializer(item, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def save_message(request):
    serializer = SendMessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
