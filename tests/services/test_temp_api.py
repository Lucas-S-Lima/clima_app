from django.test import TestCase
from unittest.mock import patch
from open_meteo_api.services.api_temp import get_temperature_from_coordinates 

class GetTemperatureTestCase(TestCase):


    @patch('open_meteo_api.services.api_temp.requests.get')
    def test_temp_api(self, mock_get):

        data = {
            'current_weather': {
                'temperature': 18
            }}
        
        response = mock_get.return_value
        response.json.return_value = data
        
        lat = '-23.54'
        lon = '-46.63'

        result = get_temperature_from_coordinates(lat, lon)

        self.assertEqual(result, 18.0)
    


