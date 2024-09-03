from django.core.exceptions import ValidationError
from django.forms import ModelForm, CheckboxInput, forms
from django.utils import timezone

from diagnostics.models import Doctor, Appointment, Service, Result


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, CheckboxInput):
                field.widget.attrs['class'] = 'form-control'


class DoctorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'


class ServiceForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class AppointmentForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

    def clean_time(self):
        time = self.cleaned_data['time']
        occupied_time = ["23:00"]
        if time in occupied_time:
            raise forms.ValidationError('Это время недоступно для записи')
        return time

    def clean_date(self):
        date = self.cleaned_data['date']
        current_date = timezone.now().date()
        if date < current_date:
            raise ValidationError('Нельзя указывать дату в прошлом')
        return date


class ResultForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Result
        fields = '__all__'
