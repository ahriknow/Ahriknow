from django.urls import path
from . import userinfo, views, jur

urlpatterns = [
    path('userinfo/', userinfo.UserinfoView.as_view()),
    path('user/', views.UserView.as_view()),
    path('user/<id>/', views.UserView.as_view()),
    path('jur/', jur.JurView.as_view()),
]
