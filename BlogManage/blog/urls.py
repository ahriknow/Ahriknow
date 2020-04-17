from django.urls import path
from . import views_category, views_tag, views_upload

urlpatterns = [
    path('category/', views_category.CategoryView.as_view()),
    path('category/<id>/', views_category.CategoryView.as_view()),
    path('tag/', views_tag.TagView.as_view()),
    path('tag/<id>/', views_tag.TagView.as_view()),
    path('upload/', views_upload.UploadView.as_view()),
]
