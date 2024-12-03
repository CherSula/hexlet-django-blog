from django.urls import path
from hexlet_django_blog.article.views import Index, ArticleView


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<int:id>/', ArticleView.as_view(), name='article')
]
