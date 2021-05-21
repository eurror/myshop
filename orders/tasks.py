from django.core.mail import send_mail
from .models import Order
from celery import task

@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order number: {order.id}'
    message = f'Dear {order.first_name}, \n\nYou have successfully placed an order.\
        Your order id is {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'edgarpo0401@gmail.com',
                          [order.email])
    return mail_sent