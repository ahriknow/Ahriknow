from django.urls import path, include

urlpatterns = [
    path('setting/', include('SettingManage.setting.urls')),
]
