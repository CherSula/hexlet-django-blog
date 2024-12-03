from django.urls import path
from hexlet_django_blog.article.views import Index, ArticleView, ArticleCommentsView


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<int:id>/', ArticleView.as_view(), name='article'),
    path('<int:article_id>/comments/<int:id>/', ArticleCommentsView.as_view())
]
