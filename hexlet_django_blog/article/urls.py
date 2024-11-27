from django.urls import path
from hexlet_django_blog.article.views import Index


urlpatterns = [
    path('', Index.as_view()),
    path('', Index.home, name='home'),
    path('<str:tags>/<int:article_id>/', Index.as_view(), name='article')
]
