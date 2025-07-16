from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomUserCreationFormProfile
from django.contrib.auth import get_user_model


User = get_user_model()

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('WebView')
    template_name = 'registration/signup.html'


class CreateViewProfile(UpdateView):
    model = User
    form_class = CustomUserCreationFormProfile
    success_url = reverse_lazy('WebView')
    template_name = 'profile.html'
    
    def get_object(self, queryset = None):
        return self.request.user