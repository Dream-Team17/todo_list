from django.urls import path
from .views import TaskListCreatAPIView, TaskGetPutDeleteAPIView
urlpatterns = [
    path('tasks/', TaskListCreatAPIView.as_view()),
    path('tasks/<int:pk>/', TaskGetPutDeleteAPIView.as_view())
]


