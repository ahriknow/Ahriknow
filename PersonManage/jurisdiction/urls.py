from django.urls import path
from . import views

urlpatterns = [
    path('jurisdiction/', views.JurisdictionView.as_view()),
    path('jurisdiction/<id>/', views.JurisdictionView.as_view()),
]
