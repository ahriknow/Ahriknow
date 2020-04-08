from django.urls import path, include

urlpatterns = [
    path('setting/', include('SettingIndex.setting-index.urls')),
]
