from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.BookView.as_view()),
    path('book/<id>/', views.BookView.as_view()),
]
