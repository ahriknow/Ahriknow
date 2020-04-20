from django.urls import path
from . import views_tab, views_article, views_comment

urlpatterns = [
    path('tab/', views_tab.TabView.as_view()),
    path('article/', views_article.ArticleView.as_view()),
    path('article/<id>/', views_article.ArticleView.as_view()),
    path('comment/<id>/', views_comment.CommentView.as_view()),
]
