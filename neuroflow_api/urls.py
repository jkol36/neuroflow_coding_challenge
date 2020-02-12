from django.urls import path
from api import views
from django.conf.urls import include

urlpatterns = [
    path('moods/', views.MoodList.as_view()),
    path('moods/<int:pk>/', views.MoodDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]