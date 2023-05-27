from django.urls import path
from tasks import views

urlpatterns = [
    path('create_task/', views.CreateTaskView),
    path('get_task/<str:task_id>/', views.GetTaskView),
    path('get_task_executor/<str:task_executor_id>/', views.GetTaskExecutorView),
    path('get_tasks/', views.GetAllTasksView),
    path('update_task/<str:task_id>/', views.PutTaskView),
    path('delete_task/<str:task_id>/', views.DeleteTaskView),
]
