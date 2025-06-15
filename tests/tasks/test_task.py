import ipdb
from django.test import TestCase
from unittest.mock import patch
from open_meteo_api.tasks import register_alert
from open_meteo_api.models import Alert


class RegisterAlertTestCase(TestCase):

    @patch('open_meteo_api.tasks.get_temperature_from_coordinates')
    @patch('open_meteo_api.tasks.get_coordinates_from_city')
    @patch('open_meteo_api.tasks.send_mail')   
    def test_register_alert_and_sends_email(self, mock_send_mail, mock_get_coord, mock_get_temp):
        
        response_coord = [{
            'lat': '-23.5400011', 
            'lon': '-46.6300011'
        }]
        mock_get_coord.return_value.json.return_value = response_coord
        
        response_temp = {
            'current_weather': {
                'temperature': 31
            }}
        
        mock_get_temp.return_value.json.return_value = response_temp

        Alert.objects.create(
            message = 'Alerta',
            email = 'test@email.com',
            temperature = 30,
            operator = '>',
            active = True,
        )
        result = register_alert.delay("São Paulo").get()
        ipdb.set_trace()

        assert result > 30
        mock_send_mail.assert_not_called()
    

    @patch('open_meteo_api.tasks.get_temperature_from_coordinates')
    @patch('open_meteo_api.tasks.get_coordinates_from_city')
    @patch('open_meteo_api.tasks.send_mail')   
    def test_register_alert_and_not_sends_mail(self, mock_send_mail, mock_get_coord, mock_get_temp):

        
        response_coord = [{
            'lat': '-23.5400011', 
            'lon': '-46.6300011'
        }]
        mock_get_coord.return_value.json.return_value = response_coord
        
        response_temp = {
            'current_weather': {
                'temperature': 29
            }}
        
        mock_get_temp.return_value.json.return_value = response_temp

        Alert.objects.create(
            message = 'Alerta',
            email = 'test@email.com',
            temperature = 30,
            operator = '>',
            active = True,
        )

        result = register_alert.delay("São Paulo").get()

        assert result > 30
        mock_send_mail.assert_not_called()
