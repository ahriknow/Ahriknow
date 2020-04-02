from django.urls import path
from . import views, catalog, content

urlpatterns = [
    path('book/', views.BookView.as_view()),
    path('book/<id>/', views.BookView.as_view()),
    path('catalog/', catalog.CatalogView.as_view()),
    path('catalog/<id>/', catalog.CatalogView.as_view()),
    path('content/<id>/', content.ContentView.as_view()),
]
