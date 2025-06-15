from django.test import TestCase
from open_meteo_api.models import City


class CityModelTestCase(TestCase):
    
    def test_register_city(self):
    
        city = City.objects.create(city = 'Teste')
        self.assertEqual(city.city, 'Teste')