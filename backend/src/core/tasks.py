import string
from celery import shared_task
import logging
from django.core.mail import 


logger = logging.getLogger(__name__)

@shared_task
def queue_messege(msg):
    print("This Morse Code Messege added to Queue ... \n msg={}".format(msg))
    logger.info("added to Queue ... \n msg={}".format(msg))


@shared_task
def send_verification_email(subject, message, host_email, recipients):
    send_mail(subject=subject, body=message,
                                 from_email=host_email, to=recipients)