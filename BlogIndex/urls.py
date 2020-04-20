from django.urls import path, include

urlpatterns = [
    path('blog/', include('BlogIndex.blog_index.urls')),
]
