from django.urls import path, include

urlpatterns = [
    path('database/', include('DatabaseManage.database.urls')),
]
