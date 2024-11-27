# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse


class Index(View):

    def get(self, request, tags, article_id):
        # return HttpResponse('article')
        tags = ['статьи', 'articles', 'article', 'статья']
        return render(
            request,
            'index.html',
            context={'tags': tags, 'article_id': article_id},
        )

    def home(self, request):
        return redirect(reverse('article', args=['python', 42]))