from django.urls import path
from . import views_tab, views_category, views_tag, views_upload, views_article, views_comment, views_follow, \
    views_fabulous

urlpatterns = [
    path('category/', views_category.CategoryView.as_view()),
    path('category/<id>/', views_category.CategoryView.as_view()),
    path('tab/', views_tab.TabView.as_view()),
    path('tab/<id>/', views_tab.TabView.as_view()),
    path('tag/', views_tag.TagView.as_view()),
    path('tag/<id>/', views_tag.TagView.as_view()),
    path('upload/', views_upload.UploadView.as_view()),
    path('article/', views_article.ArticleView.as_view()),
    path('article/<id>/', views_article.ArticleView.as_view()),
    path('comment/', views_comment.CommentView.as_view()),
    path('comment/<id>/', views_comment.CommentView.as_view()),
    path('follow/', views_follow.FollowView.as_view()),
    path('fabulous/', views_fabulous.FabulousView.as_view()),
]
