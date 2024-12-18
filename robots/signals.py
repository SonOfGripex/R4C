from django.db.models.signals import post_save
from django.dispatch import receiver
from robots.models import Robot
from orders.models import Order
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=Robot)
def robot_created_handler(sender, instance, created, **kwargs):
    orders = Order.objects.select_related('customer').filter(
        robot_serial=instance.serial
    ).values_list('customer__email', flat=True)

    if orders:
        subject = f"Робот {instance.model}, версия {instance.version}, теперь в наличии!"
        message_template = (
            "Добрый день!\n\n"
            "Недавно вы интересовались нашим роботом модели {model}, версии {version}. "
            "Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами.\n\n"
        )
        message = message_template.format(model=instance.model, version=instance.version)

        for email in orders:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )