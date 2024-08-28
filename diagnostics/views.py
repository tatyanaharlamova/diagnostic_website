from django.views.generic import TemplateView, ListView

from diagnostics.models import Doctor


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

