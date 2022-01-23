from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = "E'lonlar"
    template_name = 'main/index.html'
