from django.urls import path
from . import views

urlpatterns = [
    path('db/', views.DatabaseView.as_view()),
    path('db/<id>/', views.DatabaseView.as_view()),
]
