from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from .tasks import send_verification_email
from src.config import settings


@receiver(post_save, sender=User)
def verifiy_user_email(sender, instance, created, **kwargs):
    if created:
            subject = 'Thanks'
            message = 'body'
            recipients = [instance.email,]
            host_email = settings.EMAIL_HOST_USER

            send_verification_email.delay(subject=subject, body=message,
                                 from_email=host_email, to=recipients)