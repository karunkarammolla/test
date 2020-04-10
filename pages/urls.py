from django.urls import path
from .views import homePageView,aboutView



urlpatterns = [
    path('', homePageView, name='home'),
    path('', aboutView, name='about'),
]
