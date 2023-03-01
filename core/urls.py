from django.urls import path
from django import views
from .views import HomeTemplateView

urlpatterns = [
    path('',HomeTemplateView.as_view()),
]