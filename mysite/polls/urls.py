from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<pk>/', views.PollDetailView.as_view(),name='poll-detail')
]
