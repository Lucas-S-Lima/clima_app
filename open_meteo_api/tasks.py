import logging
from django.core.mail import send_mail
from open_meteo_api.services.api_coord import get_coordinates_from_city
from open_meteo_api.services.api_temp import get_temperature_from_coordinates
from .models import Alert, Temperature, City
from celery import shared_task


logger = logging.getLogger(__name__)

@shared_task
def register_alert(name_city):

    logging.basicConfig(filename='tasks.log', level=logging.INFO)

    lat, lon = get_coordinates_from_city(name_city)
    current_temperature = get_temperature_from_coordinates(lat, lon)

    city, created = City.objects.get_or_create(city=name_city)

    temperature = Temperature.objects.create(
        temperature=current_temperature,
        city=city
    )
    
    alerts = Alert.objects.filter(active=True)
        
    for alert in alerts:
        if (temperature.temperature > alert.temperature) and (alert.operator == '>'):

            logger.warning('Temperatura subindo')

            send_mail(
                "Alerta de onda de calor",
                alert.message,
                "2ucas2ima@gmail.com",
                [alert.email],
                fail_silently=False,
            )

            logger.info(f'Email enviado com sucesso para a cidade de {city}')

            
        elif (temperature.temperature < alert.temperature) and (alert.operator == '<'):

            logger.warning('Temperatura caindo')

            send_mail(
                "Alerta de frente fria",
                alert.message,
                "2ucas2ima@gmail.com",
                [alert.email],
                fail_silently=False,
            )

            logger.info(f'Email enviado com sucesso para a cidade de {city}')

    return float(current_temperature)
    
    




