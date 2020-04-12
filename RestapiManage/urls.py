from django.urls import path, include

urlpatterns = [
    path('restapi/', include('RestapiManage.restapi.urls')),
]
