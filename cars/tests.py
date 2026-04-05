from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from cars.models import Car, Manufacturer, Category
from cars.validators import validate_car_year, validate_car_vin
from django.core.exceptions import ValidationError

# Create your tests here.

Profile = get_user_model()

class CarModelTest(TestCase):
    def setUp(self):
        self.user = Profile.objects.create_user(username='testuser', password='testpass123')
        self.manufacturer = Manufacturer.objects.create(name='Toyota', country='Japan')
        self.car = Car.objects.create(
            name='Corolla',
            manufacturer=self.manufacturer,
            year=2020,
            vin='1HGBH41JXMN109186',
            owner=self.user
        )

    def test_car_age(self):
        from datetime import date
        expected_age = date.today().year - 2020
        self.assertEqual(self.car.age(), expected_age)

    def test_car_str(self):
        self.assertIn('Corolla', str(self.car))

    def test_total_maintenance_cost_no_records(self):
        self.assertEqual(self.car.total_maintenance_cost(), 0)

    def test_vin_saved_uppercase(self):
        self.assertEqual(self.car.vin, self.car.vin.upper())


class CarValidatorTest(TestCase):
    def test_year_in_future_raises(self):
        with self.assertRaises(ValidationError):
            validate_car_year(2999)

    def test_year_too_old_raises(self):
        with self.assertRaises(ValidationError):
            validate_car_year(1800)

    def test_valid_year_passes(self):
        validate_car_year(2020)

    def test_vin_wrong_length_raises(self):
        with self.assertRaises(ValidationError):
            validate_car_vin('SHORT')

    def test_vin_invalid_chars_raises(self):
        with self.assertRaises(ValidationError):
            validate_car_vin('1HGBH41JXMN10918I')

class CarViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = Profile.objects.create_user(username='testuser', password='testpass123')
        self.manufacturer = Manufacturer.objects.create(name='Toyota', country='Japan')
        self.car = Car.objects.create(
            name='Corolla',
            manufacturer=self.manufacturer,
            year=2020,
            vin='1HGBH41JXMN109186',
            owner=self.user
        )

    def test_car_list_view_returns_200(self):
        response = self.client.get(reverse('cars:list'))
        self.assertEqual(response.status_code, 200)

    def test_car_detail_view_returns_200(self):
        response = self.client.get(reverse('cars:detail', kwargs={'pk': self.car.pk}))
        self.assertEqual(response.status_code, 200)

    def test_car_create_requires_login(self):
        response = self.client.get(reverse('cars:add'))
        self.assertEqual(response.status_code, 302)

    def test_car_create_logged_in(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('cars:add'))
        self.assertEqual(response.status_code, 200)

    def test_other_user_cannot_delete_car(self):
        other_user = Profile.objects.create_user(username='other', password='testpass123')
        self.client.login(username='other', password='testpass123')
        response = self.client.post(reverse('cars:delete', kwargs={'pk': self.car.pk}))
        self.assertEqual(response.status_code, 404)