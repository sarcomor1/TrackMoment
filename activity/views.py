from django.views.generic import CreateView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import ActivityForms
from .models import ActivityModels

class CreateActivityView(LoginRequiredMixin, CreateView):
    model = ActivityModels
    form_class = ActivityForms
    template_name = 'addactivity.html'
    success_url = reverse_lazy('myprofile')

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)

class MyActivitiesListView(LoginRequiredMixin, ListView):
    model = ActivityModels
    template_name = 'myprofile.html'
    context_object_name = 'activities'

    def get_queryset(self):
        return ActivityModels.objects.filter(user_id=self.request.user)
    
class ActivityUpdateView(UpdateView):
    model = ActivityModels
    template_name = 'activity_update.html'
    fields = ['activity_type', 'activity_details', 'location', 'activity_date', 'image']
    success_url = reverse_lazy('myprofile')

class ActivityDeleteView(DeleteView):
    model = ActivityModels
    template_name = 'activity_delete.html'
    success_url = reverse_lazy('myprofile')
