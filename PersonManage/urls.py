from django.urls import path, include

urlpatterns = [
    path('person/', include('PersonManage.department.urls')),
    path('person/', include('PersonManage.jurisdiction.urls')),
    path('person/', include('PersonManage.role.urls')),
    path('person/', include('PersonManage.user.urls')),
]
