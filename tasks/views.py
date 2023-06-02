from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import Tasks
from .serializers import CreateTaskSerializer, GetTaskSerializer,\
    EmployeeGetTaskSerializer, SendTaskToCheckSerializer, AcceptTaskSerializer, ReturnTaskSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def CreateTaskView(request):
    serializer = CreateTaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def GetAllTasksView(request):
    item = Tasks.objects.all()
    serializer = GetTaskSerializer(item, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def GetTaskView(request, task_id):
    item = Tasks.objects.all.filter(id=task_id)
    serializer = GetTaskSerializer(item, many=False)
    return Response(serializer.data)\


@api_view(['GET'])
@permission_classes([AllowAny])
def GetTaskExecutorView(request, task_executor_id):
    item = Tasks.objects.filter(task_executor=task_executor_id).order_by('task_status')
    serializer = GetTaskSerializer(item, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def GetTasksWaitingView(request):
    item = Tasks.objects.filter(task_status=1)
    serializer = GetTaskSerializer(item, many=True)
    return Response(serializer.data)\


@api_view(['GET'])
@permission_classes([AllowAny])
def GetTasks_in_CheckView(request):
    item = Tasks.objects.filter(task_status=3)
    serializer = GetTaskSerializer(item, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def PutExecutorTaskView(request, task_id):
    item = Tasks.objects.get(id=task_id)
    serializer = EmployeeGetTaskSerializer(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def SendToCheckTaskView(request, task_id):
    item = Tasks.objects.get(id=task_id)
    serializer = SendTaskToCheckSerializer(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def AcceptTaskView(request, task_id):
    item = Tasks.objects.get(id=task_id)
    serializer = AcceptTaskSerializer(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ReturnTaskView(request, task_id):
    item = Tasks.objects.get(id=task_id)
    serializer = ReturnTaskSerializer(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteTaskView(request, task_id):
    try:
        item = Tasks.objects.get(id=task_id)
    except Tasks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)