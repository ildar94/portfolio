from django.views.generic.base import TemplateView
# Create your views here.

class Index_page(TemplateView):
    template_name = 'blog/index.html'


class Backend_page(TemplateView):
    template_name = 'blog/backend_page.html'

class Frontend_page(TemplateView):
    template_name = 'blog/frontend_page.html'
