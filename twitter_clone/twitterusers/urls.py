from django.urls import path
from . import views


urlpatterns = [
    path('user/new/', views.create_new_user, name="new_user"),
    path('user/<int:user_id>', views.user_detail, name="user_detail"),
]