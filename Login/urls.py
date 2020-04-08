from django.urls import path
from . import views, signup

urlpatterns = [
    path('login/', views.AuthView.as_view()),
    path('signup/', signup.UserView.as_view()),
]
