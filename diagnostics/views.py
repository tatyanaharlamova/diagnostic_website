from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from diagnostics.forms import DoctorForm, ServiceForm, AppointmentForm, ResultForm
from diagnostics.models import Doctor, Service, Appointment, Result


class HomeView(TemplateView):
    """
    Контроллер главной страницы сайта
    """
    template_name = 'diagnostics/index.html'


class DoctorListView(ListView):
    """
    Контроллер отвечающий за отображение списка врачей
    """
    model = Doctor


class DoctorDetailView(DetailView):
    """
    Контроллер, который отвечает за отображение информации о враче
    """
    model = Doctor


class DoctorCreateView(CreateView):
    """
    Контроллер, который отвечает за создание врача
    """
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy('diagnostics:doctors_list')


class DoctorUpdateView(UpdateView):
    """
    Контроллер, который отвечает за редактирование врача
    """
    model = Doctor
    form_class = DoctorForm

    def get_success_url(self):
        return reverse('diagnostics:doctor_detail', args=[self.kwargs.get('pk')])


class DoctorDeleteView(DeleteView):
    """
    Контроллер, который отвечает за удаление врача
    """
    model = Doctor
    success_url = reverse_lazy('diagnostics:doctors_list')


class ServiceListView(ListView):
    """
    Контроллер отвечающий за отображение списка услуг
    """
    model = Service


class ServiceDetailView(DetailView):
    """
    Контроллер, который отвечает за отображение информации об услуге
    """
    model = Service


class ServiceCreateView(CreateView):
    """
    Контроллер, который отвечает за создание услуги
    """
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('diagnostics:services_list')


class ServiceUpdateView(UpdateView):
    """
    Контроллер, который отвечает за редактирование услуги
    """
    model = Service
    form_class = ServiceForm

    def get_success_url(self):
        return reverse('diagnostics:service_detail', args=[self.kwargs.get('pk')])


class ServiceDeleteView(DeleteView):
    """
    Контроллер, который отвечает за удаление услуги
    """
    model = Service
    success_url = reverse_lazy('diagnostics:services_list')


class AppointmentListView(ListView):
    """
    Контроллер отвечающий за отображение списка записей
    """
    model = Appointment


class AppointmentDetailView(DetailView):
    """
    Контроллер, который отвечает за отображение информации о записи
    """
    model = Appointment


class AppointmentCreateView(CreateView):
    """
    Контроллер, который отвечает за создание записи
    """
    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy('diagnostics:appointments_list')


class AppointmentUpdateView(UpdateView):
    """
    Контроллер, который отвечает за редактирование записи
    """
    model = Appointment
    form_class = AppointmentForm

    def get_success_url(self):
        return reverse('diagnostics:appointment_detail', args=[self.kwargs.get('pk')])


class AppointmentDeleteView(DeleteView):
    """
    Контроллер, который отвечает за удаление записи
    """
    model = Appointment
    success_url = reverse_lazy('diagnostics:appointments_list')


class ResultListView(ListView):
    """
    Контроллер отвечающий за отображение списка результатов
    """
    model = Result


class ResultCreateView(CreateView):
    """
    Контроллер, который отвечает за создание результата
    """
    model = Result
    form_class = ResultForm
    success_url = reverse_lazy('diagnostics:results_list')


class ResultUpdateView(UpdateView):
    """
    Контроллер, который отвечает за редактирование результата
    """
    model = Result
    form_class = ResultForm
    success_url = reverse_lazy('diagnostics:results_list')


class ResultDeleteView(DeleteView):
    """
    Контроллер, который отвечает за удаление записи
    """
    model = Result
    success_url = reverse_lazy('diagnostics:appointments_list')
