from django.urls import path
from .views import WebView

urlpatterns = [
    path('', WebView.as_view(), name= 'WebView'),
]