from django.urls import path, include

urlpatterns = [
    path('notebook/', include('NotebookManage.notebook.urls')),
]
