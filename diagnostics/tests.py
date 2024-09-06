from django.test import TestCase

from diagnostics.models import Doctor, Service, Appointment, Result
from users.models import User


class DoctorTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@example.com")
        self.doctor = Doctor.objects.create(name='Иванов Иван Иванович', specialization='Хирург')

    def test_doctor_detail(self):
        doctor = Doctor.objects.get(name="Иванов Иван Иванович")
        self.assertEqual(doctor.specialization, 'Хирург')

    def test_doctor_list(self):
        doctors_count = Doctor.objects.all().count()
        self.assertEqual(doctors_count, 1)

    def test_doctor_update(self):
        doctor = Doctor.objects.get(name="Иванов Иван Иванович")
        doctor.specialization = 'ЛОР'
        self.assertEqual(doctor.specialization, 'ЛОР')

    def test_doctor_create(self):
        Doctor.objects.create(name='Петров Петр Петрович', specialization='ЛОР')
        doctors_count = Doctor.objects.all().count()
        self.assertEqual(doctors_count, 2)

    def test_doctor_delete(self):
        doctor = Doctor.objects.get(name="Иванов Иван Иванович")
        doctor.delete()
        doctors_count = Doctor.objects.all().count()
        self.assertEqual(doctors_count, 0)


class ServiceTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@example.com")
        self.service = Service.objects.create(service_name='УЗИ', price=2000)

    def test_service_detail(self):
        service = Service.objects.get(service_name="УЗИ")
        self.assertEqual(service.price, 2000)

    def test_service_list(self):
        services_count = Service.objects.all().count()
        self.assertEqual(services_count, 1)

    def test_service_update(self):
        service = Service.objects.get(service_name="УЗИ")
        service.price = 1500
        self.assertEqual(service.price, 1500)

    def test_service_create(self):
        self.service = Service.objects.create(service_name='КТ', price=5000)
        services_count = Service.objects.all().count()
        self.assertEqual(services_count, 2)

    def test_service_delete(self):
        service = Service.objects.get(service_name="УЗИ")
        service.delete()
        services_count = Service.objects.all().count()
        self.assertEqual(services_count, 0)


class AppointmentTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@example.com")
        self.doctor = Doctor.objects.create(name='Иванов Иван Иванович', specialization='Хирург')
        self.appointment = Appointment.objects.create(date='2024-09-20', time='12:00', doctor=self.doctor,
                                                      owner=self.user)

    def test_appointment_detail(self):
        appointment = Appointment.objects.get(owner=self.user)
        self.assertEqual(appointment.doctor.name, 'Иванов Иван Иванович')

    def test_appointment_list(self):
        appointment_count = Appointment.objects.all().count()
        self.assertEqual(appointment_count, 1)

    def test_appointment_update(self):
        appointment = Appointment.objects.get(owner=self.user)
        appointment.doctor.name = 'Петров Петр Петрович'
        self.assertEqual(appointment.doctor.name, 'Петров Петр Петрович')

    def test_appointment_create(self):
        self.appointment = Appointment.objects.create(date='2024-10-20', time='12:00', doctor=self.doctor,
                                                      owner=self.user)

        appointment_count = Appointment.objects.all().count()
        self.assertEqual(appointment_count, 2)

    def test_appointment_delete(self):
        appointment = Appointment.objects.get(owner=self.user)
        appointment.delete()
        appointment_count = Appointment.objects.all().count()
        self.assertEqual(appointment_count, 0)


class ResultTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@example.com")
        self.result = Result.objects.create(test='Общий билирубин', date='2024-10-20', result="24")

    def test_result_detail(self):
        result = Result.objects.get(test='Общий билирубин')
        self.assertEqual(result.result, '24')

    def test_result_list(self):
        results_count = Result.objects.all().count()
        self.assertEqual(results_count, 1)

    def test_result_update(self):
        result = Result.objects.get(test='Общий билирубин')
        result.result = '15'
        self.assertEqual(result.result, '15')

    def test_result_create(self):
        self.result = Result.objects.create(test='СРБ', date='2024-10-20', result="2")
        results_count = Result.objects.all().count()
        self.assertEqual(results_count, 2)

    def test_appointment_delete(self):
        result = Result.objects.get(test='Общий билирубин')
        result.delete()
        results_count = Result.objects.all().count()
        self.assertEqual(results_count, 0)
