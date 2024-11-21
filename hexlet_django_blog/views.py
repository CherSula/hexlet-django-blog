from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    self.template_name = 'index.html'

    def get_context_data(self, **kwargs):
        self.context = super().get_context_data(**kwargs)
        self.context['who'] = 'World'
        return self.context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)


def about(request):
    # return render(request, 'about.html')
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(
        request,
        'about.html',
        context={'tags': tags},
    )
