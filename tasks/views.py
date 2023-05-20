from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Task
from .serializers import CreateTaskSerializer, GetTaskSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateTaskView(request):
    serializer = CreateTaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetAllTasksView(request):
    item = Task.objects.all()
    serializer = GetTaskSerializer(item, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetTaskView(request, task_id):
    item = Task.objects.all.filter(id=task_id)
    serializer = GetTaskSerializer(item, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def PutTaskView(request, task_id):
    item = Task.objects.get(id=task_id)
    serializer = CreateTaskSerializer(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteTaskView(request, task_id):
    try:
        item = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)