from django.test import TestCase
from open_meteo_api.models import Temperature, City


class TemperatureModelTestCase(TestCase):

    def test_register_temperature(self):
        city = City.objects.create(city = 'Teste')

        temperature = Temperature.objects.create(
            temperature = 9.5,
            city = city
        )

        self.assertEqual(temperature.temperature, 9.5)
        self.assertEqual(temperature.city, city)
