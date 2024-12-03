# from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse
from hexlet_django_blog.article.models import Article


class Index(View):

    # def get(self, request, tags, article_id):
    #     # return HttpResponse('article')
    #     tags = ['статьи', 'articles', 'article', 'статья']
    #     return render(
    #         request,
    #         'index.html',
    #         context={'tags': tags, 'article_id': article_id},
    #     )

    # def home(self, request):
    #     return redirect(reverse('article', args=['python', 42]))

    def get(self, request):
        articles = Article.objects.all()
        print(articles)
        return render(request, "articles/index.html", context={"articles": articles})


class ArticleView(View):
    def get(self, request, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(request, "articles/show.html", context={"article": article})
