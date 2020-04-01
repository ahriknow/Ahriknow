from django.urls import path
from . import auth, views, jur

urlpatterns = [
    path('auth/', auth.AuthView.as_view()),
    path('auth/<id>/', auth.AuthView.as_view()),
    path('user/', views.UserView.as_view()),
    path('user/<id>/', views.UserView.as_view()),
    path('jur/', jur.JurView.as_view()),
    path('jur/<id>/', jur.JurView.as_view()),
]
