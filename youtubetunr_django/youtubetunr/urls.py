from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('youtubers/', views.YoutuberList.as_view(), name='youtuber_list'),
    path('youtubers/<int:pk>', views.YoutuberDetail.as_view(), name='youtuber_detail')
]
