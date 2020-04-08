from django.urls import path
from . import views

urlpatterns = [
    path('index-show/', views.IndexShowView.as_view()),
]
