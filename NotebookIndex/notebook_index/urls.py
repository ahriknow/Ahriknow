from django.urls import path
from . import views_book, views_catalog, views_content, views_tag

urlpatterns = [
    path('book/', views_book.BookView.as_view()),
    path('tag/', views_tag.TagView.as_view()),
    path('catalog/<id>/', views_catalog.CatalogView.as_view()),
    path('content/<id>/', views_content.ContentView.as_view()),
]
