from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "pages/home.html"  #* Template for the home page

class AboutPageView(TemplateView):
    template_name = "pages/about.html"  #* Template for the about page