from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import CustomUser
from .serializers import UserInfoSerializer, UserFillInfoSerializer, AllUsersSerializer,Edit_Employee_Serializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userinfo(request, user_id):
    item = CustomUser.objects.get(id=user_id)
    serializer = UserInfoSerializer(item, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def allusers(request):
    item = CustomUser.objects.all()
    serializer = AllUsersSerializer(item, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def filluserinfo(request, user_id):
    item = CustomUser.objects.get(id=user_id)
    serializer = UserFillInfoSerializer(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_employee(request, user_id):
    item = CustomUser.objects.get(id=user_id)
    serializer = Edit_Employee_Serializer(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
