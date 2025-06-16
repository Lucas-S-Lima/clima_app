from django.test import TestCase
from unittest.mock import patch
from open_meteo_api.tasks import register_alert
from open_meteo_api.models import Alert


class RegisterAlertTestCase(TestCase):

    @patch('open_meteo_api.tasks.get_temperature_from_coordinates')
    @patch('open_meteo_api.tasks.get_coordinates_from_city')
    @patch('open_meteo_api.tasks.send_mail')   
    def test_register_alert_and_sends_email(self, mock_send_mail, mock_get_coord, mock_get_temp):

        mock_get_coord.return_value = ('-23.540', '-46.630')
           
        mock_get_temp.return_value = 31

        Alert.objects.create(
            message='Alerta',
            email='test@email.com',
            temperature=30,
            operator='>',
            active=True,
        )
        result = register_alert("São Paulo")

        assert result > 30
        mock_send_mail.assert_called_once()
    
    @patch('open_meteo_api.tasks.get_temperature_from_coordinates')
    @patch('open_meteo_api.tasks.get_coordinates_from_city')
    @patch('open_meteo_api.tasks.send_mail')   
    def test_register_alert_and_not_sends_mail(self, mock_send_mail, mock_get_coord, mock_get_temp):
    
        mock_get_coord.return_value = ('-23.540', '-46.630')
           
        mock_get_temp.return_value = 29

        Alert.objects.create(
            message='Alerta',
            email='test@email.com',
            temperature=30,
            operator='>',
            active=True,
        )

        result = register_alert("São Paulo")

        assert result < 30
        mock_send_mail.assert_not_called()
