from django.urls import path

from diagnostics.apps import DiagnosticsConfig
from diagnostics.views import HomeView, DoctorListView

app_name = DiagnosticsConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('clients_list/', DoctorListView.as_view(), name='doctors_list')
]
