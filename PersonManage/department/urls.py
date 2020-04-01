from django.urls import path
from . import views

urlpatterns = [
    path('department/', views.DepartmentView.as_view()),
    path('department/<id>/', views.DepartmentView.as_view()),
]
