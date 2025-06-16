from django.test import TestCase
from unittest.mock import patch
from open_meteo_api.services.api_coord import get_coordinates_from_city


class GetCoordinatesTestCase(TestCase):

    @patch('open_meteo_api.services.api_temp.requests.get')
    def test_temp_api(self, mock_get):

        data = [{
            'lat': '-23.5400011', 
            'lon': '-46.6300011'
        }]

        response = mock_get.return_value
        response.json.return_value = data
        
        city = "São Paulo"
        
        result = get_coordinates_from_city(city)

        self.assertEqual(result[0], '-23.540')
        self.assertEqual(result[1], '-46.630')
    