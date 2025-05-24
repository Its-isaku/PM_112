
#? Importing necessary modules
from django.urls import path
from .views import HomePageView, AboutPageView

#? URL patterns for the pages app
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  #* URL pattern for the home page
    path('about/', AboutPageView.as_view(), name='about'),  #* URL pattern for the about page
]
