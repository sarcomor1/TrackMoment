from django.views.generic import TemplateView

class WebView(TemplateView):
    template_name = 'home.html'
    