from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from cars.models import Car, Manufacturer
from parts.models import Part
from parts.validators import validate_part_price

# Create your tests here.

Profile = get_user_model()

class PartValidatorTest(TestCase):
    def test_negative_price_raises(self):
        with self.assertRaises(ValidationError):
            validate_part_price(-5)

    def test_zero_price_passes(self):
        validate_part_price(0)

    def test_positive_price_passes(self):
        validate_part_price(99.99)


class PartViewTest(TestCase):
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
        self.part = Part.objects.create(
            name='Oil Filter',
            manufacturer='Bosch',
            price=19.99,
            owner=self.user
        )

    def test_parts_list_requires_login(self):
        response = self.client.get(reverse('parts:list'))
        self.assertEqual(response.status_code, 302)

    def test_parts_list_logged_in(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('parts:list'))
        self.assertEqual(response.status_code, 200)

    def test_other_user_cannot_see_part(self):
        self.client.login(username='other', password='testpass123')
        response = self.client.get(reverse('parts:detail', kwargs={'pk': self.part.pk}))
        self.assertEqual(response.status_code, 404)

    def test_part_str(self):
        self.assertIn('Oil Filter', str(self.part))