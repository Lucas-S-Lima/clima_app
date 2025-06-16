from django.test import TestCase
from open_meteo_api.models import Alert, City


class AlertModelTestCase(TestCase):

    def test_register_alert(self):
        city = City.objects.create(city='Teste')
        
        alert = Alert.objects.create(
            city=city,
            operator='>',
            temperature=36,
            message='Alerta de tempo quente!',
            active=True,
            email='email@test.com',

        )

        self.assertEqual(alert.city, city)
        self.assertEqual(alert.temperature, 36)
        self.assertEqual(alert.operator, '>')
        self.assertEqual(alert.message, 'Alerta de tempo quente!')
        self.assertTrue(alert.active)
        self.assertEqual(alert.email, 'email@test.com')
