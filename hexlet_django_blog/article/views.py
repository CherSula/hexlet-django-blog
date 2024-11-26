# from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class IndexView(View):

    def get(self, request):
        # return HttpResponse('article')
        tags = ['статьи', 'articles', 'article', 'статья']
        return render(
            request,
            'index.html',
            context={'tags': tags},
        )
