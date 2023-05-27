from django.urls import path
from users import views

urlpatterns = [
    path('info/<str:user_id>/', views.userinfo),
    path('fillinfo/<str:user_id>/',views.filluserinfo),
    path('all_users',views.allusers),
]
