# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse('article')
    tags = ['статьи', 'articles', 'article', 'статья']
    return render(
        request,
        'index.html',
        context={'tags': tags},
    )
