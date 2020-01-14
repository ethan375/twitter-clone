from django.urls import path
from . import views


urlpatterns = [
    path('user/new/', views.create_new_user, name="new_user"),
    path('user/<int:user_id>', views.user_detail, name="user_detail"),
    path('user/follow/<int:loggedin_user>/<int:following_user>', views.follow_user, name="follow_user")
]