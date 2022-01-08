from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from django.core.mail import send_mail
from django.http import HttpResponse

from .views import get_temperature, set_emoji
from .models import Receiver


@receiver(post_save, sender=Receiver)
def email_send(sender, instance, **kwargs):
    temperature = get_temperature(instance.city)
    if temperature:
        emoji = set_emoji(temperature)
        try:
            send_mail(
                subject=f'Hi {instance.full_name}, interested in our services',
                message= f'Hello {instance.full_name} the temperature of {instance.city} at {instance.created.strftime("%Y-%m-%d %H:%M:%S")} is {temperature} in Kelvin {emoji}',
                from_email='owaisbhat996@gmail.com',
                recipient_list=[instance.email],
                fail_silently=True
            )
            return HttpResponse(200)
        except:
            return HttpResponse('Error sending mail')
    else:
        return HttpResponse('An error occured in geting temperature.')
    