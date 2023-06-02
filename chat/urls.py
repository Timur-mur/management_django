from django.urls import path
from chat import views

urlpatterns = [
    path('get_messages', views.get_all_messages),
    path('save_message', views.save_message)
]