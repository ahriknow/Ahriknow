from django.urls import path
from . import views_project, views_url, views_opera

urlpatterns = [
    path('project/', views_project.ProjectView.as_view()),
    path('project/<id>/', views_project.ProjectView.as_view()),
    path('url/', views_url.UrlView.as_view()),
    path('url/<id>/', views_url.UrlView.as_view()),
    path('opera/<id>/', views_opera.OperaView.as_view()),
]
