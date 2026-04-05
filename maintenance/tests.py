from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from cars.models import Car, Manufacturer
from maintenance.models import MaintenanceRecord
from maintenance.validators import validate_maintenance_cost

# Create your tests here.

Profile = get_user_model()

class MaintenanceValidatorTest(TestCase):
    def test_negative_cost_raises(self):
        with self.assertRaises(ValidationError):
            validate_maintenance_cost(-10)

    def test_zero_cost_passes(self):
        validate_maintenance_cost(0)

    def test_positive_cost_passes(self):
        validate_maintenance_cost(100)

class MaintenanceViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = Profile.objects.create_user(username='testuser', password='testpass123')
        self.other_user = Profile.objects.create_user(username='other', password='testpass123')
        self.manufacturer = Manufacturer.objects.create(name='Toyota', country='Japan')
        self.car = Car.objects.create(
            name='Corolla',
            manufacturer=self.manufacturer,
            year=2020,
            vin='1HGBH41JXMN109186',
            owner=self.user
        )
        self.record = MaintenanceRecord.objects.create(
            car=self.car,
            date='2024-01-01',
            description='Oil change',
            cost=50.00,
            owner=self.user
        )

    def test_maintenance_list_requires_login(self):
        response = self.client.get(reverse('maintenance:list'))
        self.assertEqual(response.status_code, 302)

    def test_maintenance_list_logged_in(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('maintenance:list'))
        self.assertEqual(response.status_code, 200)

    def test_other_user_cannot_see_record(self):
        self.client.login(username='other', password='testpass123')
        response = self.client.get(reverse('maintenance:detail', kwargs={'pk': self.record.pk}))
        self.assertEqual(response.status_code, 404)

    def test_maintenance_str(self):
        self.assertIn('Oil change', str(self.record))