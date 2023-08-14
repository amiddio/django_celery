from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


@shared_task
def send_contact_email_task(data):
    """Celery задача для отпправки email-а"""

    try:
        msg_plain = render_to_string('app_contact/email.txt', {'data': data})
        msg_html = render_to_string('app_contact/email.html', {'data': data})
        send_mail(
            subject=data['subject'],
            message=msg_plain,
            from_email=data['email'],
            recipient_list=[settings.CONTACT_EMAIL],
            html_message=msg_html,
            fail_silently=False
        )
    except Exception:
        raise Exception("Internal server error! Your message cannot be send. Try it later.")

