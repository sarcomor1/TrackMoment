from django.urls import path
from .views import CreateActivityView, MyActivitiesListView, ActivityUpdateView,ActivityDeleteView

urlpatterns = [
    path('addactivity/', CreateActivityView.as_view(), name='addactivity'),
    path('myprofile/list/', MyActivitiesListView.as_view(), name='myprofile'),
    path('myprofile/update/<int:pk>', ActivityUpdateView.as_view(), name='update'),
    path('myprofile/delete/<int:pk>', ActivityDeleteView.as_view(), name='delete'),
]
