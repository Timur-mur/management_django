from django.urls import path
from users import views

urlpatterns = [
    path('info/<str:user_id>/', views.userinfo),
    path('fillinfo/<str:user_id>/',views.filluserinfo),
    path('edit_employee/<str:user_id>/',views.edit_employee),
    path('all_users',views.allusers),
]
