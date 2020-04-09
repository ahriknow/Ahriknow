from django.urls import path, include

urlpatterns = [
    path('notebook/', include('NotebookIndex.notebook_index.urls')),
]
