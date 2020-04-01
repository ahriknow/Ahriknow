from django.urls import path
from . import views

urlpatterns = [
    path('role/', views.RoleView.as_view()),
    path('role/<id>/', views.RoleView.as_view()),
]
