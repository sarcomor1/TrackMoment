from django.views.generic import CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomUserCreationFormProfile
from django.contrib.auth import get_user_model


User = get_user_model()

class SignUpView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'


class CreateViewEmail(UpdateView):
    model = User
    form_class = CustomUserCreationFormProfile
    success_url = reverse_lazy('home')
    template_name = 'email.html'
    
    def get_object(self, queryset = None):
        return self.request.user
    
class Myprofile(TemplateView):
    template_name = 'myprofile.html'
    