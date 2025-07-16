from django.urls import path
from .views import SignUpView, CreateViewProfile

urlpatterns = [
    path('signup/', SignUpView.as_view(), name= 'signup'),
    path('profile', CreateViewProfile.as_view(), name= 'profile'),
]