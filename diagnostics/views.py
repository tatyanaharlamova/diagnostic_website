from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from diagnostics.forms import DoctorForm, ServiceForm, AppointmentForm, ResultForm, ContactForm
from diagnostics.models import Doctor, Service, Appointment, Result, Contact
from diagnostics.services import get_doctors_from_cache


class HomeView(TemplateView):
    """
    Контроллер главной страницы сайта
    """
    template_name = 'diagnostics/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        services = Service.objects.all()
        context_data['random_doctors'] = get_doctors_from_cache().order_by('?')[:3]
        context_data['all_services'] = services.order_by('?')[:3]
        return context_data


class DoctorListView(ListView):
    """
    Контроллер отвечающий за отображение списка врачей
    """
    model = Doctor

    def get_queryset(self):
        return get_doctors_from_cache()


class DoctorDetailView(DetailView):
    """
    Контроллер, который отвечает за отображение информации о враче
    """
    model = Doctor


class DoctorCreateView(CreateView, LoginRequiredMixin):
    """
    Контроллер, который отвечает за создание врача
    """
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy('diagnostics:doctors_list')


class DoctorUpdateView(UpdateView, LoginRequiredMixin):
    """
    Контроллер, который отвечает за редактирование врача
    """
    model = Doctor
    form_class = DoctorForm

    def get_success_url(self):
        return reverse('diagnostics:doctor_detail', args=[self.kwargs.get('pk')])


class DoctorDeleteView(DeleteView, LoginRequiredMixin):
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


class ServiceCreateView(CreateView, LoginRequiredMixin):
    """
    Контроллер, который отвечает за создание услуги
    """
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('diagnostics:services_list')


class ServiceUpdateView(UpdateView, LoginRequiredMixin):
    """
    Контроллер, который отвечает за редактирование услуги
    """
    model = Service
    form_class = ServiceForm

    def get_success_url(self):
        return reverse('diagnostics:service_detail', args=[self.kwargs.get('pk')])


class ServiceDeleteView(DeleteView, LoginRequiredMixin):
    """
    Контроллер, который отвечает за удаление услуги
    """
    model = Service
    success_url = reverse_lazy('diagnostics:services_list')


class AppointmentListView(ListView, LoginRequiredMixin):
    """
    Контроллер отвечающий за отображение списка записей
    """
    model = Appointment

    def get_queryset(self, queryset=None):
        queryset = super().get_queryset()
        user = self.request.user
        if not user.is_superuser and not user.groups.filter(name='moderator'):
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class AppointmentDetailView(DetailView, LoginRequiredMixin):
    """
    Контроллер, который отвечает за отображение информации о записи
    """
    model = Appointment


class AppointmentCreateView(CreateView, LoginRequiredMixin):
    """
    Контроллер, который отвечает за создание записи
    """
    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy('diagnostics:appointments_list')

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.owner = user
        mailing.save()
        return super().form_valid(form)


class AppointmentUpdateView(UpdateView, LoginRequiredMixin):
    """
    Контроллер, который отвечает за редактирование записи
    """
    model = Appointment
    form_class = AppointmentForm

    def get_success_url(self):
        return reverse('diagnostics:appointment_detail', args=[self.kwargs.get('pk')])


class AppointmentDeleteView(DeleteView, LoginRequiredMixin):
    """
    Контроллер, который отвечает за удаление записи
    """
    model = Appointment
    success_url = reverse_lazy('diagnostics:appointments_list')


class ResultListView(ListView, LoginRequiredMixin):
    """
    Контроллер отвечающий за отображение списка результатов
    """
    model = Result

    def get_queryset(self, queryset=None):
        queryset = super().get_queryset()
        user = self.request.user
        if not user.is_superuser and not user.groups.filter(name='moderator'):
            queryset = queryset.filter(owner=self.request.user)
        return queryset


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


class ContactCreateView(CreateView):
    """
    Контроллер, который отвечает за создание сообщения
    """
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy("diagnostics:contacts")
