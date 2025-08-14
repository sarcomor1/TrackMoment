from django.urls import path
from .views import SignUpView, CreateViewEmail , Myprofile

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('email/', CreateViewEmail.as_view(), name='email'),
    path('myprofile/', Myprofile.as_view(), name='myprofile'),

]
