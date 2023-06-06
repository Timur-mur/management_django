from django.urls import path
from tasks import views

urlpatterns = [
    path('create_task/', views.CreateTaskView),
    path('get_task/<str:task_id>', views.GetTaskView),
    path('get_tasks_in_waiting/', views.GetTasksWaitingView),
    path('get_task_executor/<str:task_executor_id>/', views.GetTaskExecutorView),
    path('get_tasks/', views.GetAllTasksView),
    path('employee_get_task/<str:task_id>', views.PutExecutorTaskView),
    path('tasks_in_check/', views.GetTasks_in_CheckView),
    path('send_task_to_check/<str:task_id>', views.SendToCheckTaskView),
    path('accept_task/<str:task_id>', views.AcceptTaskView),
    path('return_task/<str:task_id>', views.ReturnTaskView),
    path('delete_task/<str:task_id>', views.DeleteTaskView),
    path('count_accepted_tasks/', views.add_count_accepted_task_view),
    path('get_count_accepted_tasks/', views.get_count_acepted_task_view),
]
