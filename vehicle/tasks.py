from celery import shared_task
from django.core.mail import send_mail

from vehicle.models import Moto, Car


@shared_task
def check_milage(pk, model):
    if model == 'Car':
        obj = Car.objects.filter(pk=pk).first()
    else:
        obj = Moto.objects.filter(pk=pk).first()
        # obj = Moto.objects.get(pk=pk)

    if obj:
        prev_milage = -1
        for m in obj.milage.all():
            if prev_milage == -1:
                prev_milage = m.milage

            else:
                if prev_milage < m.milage:
                    print("Неверный пробег")
                    break


def check_filter():
    filter_price = {'price__lte': 500}

    if Car.objects.filter(**filter_price).exists():
        print('Report about filter')
        # send_mail(
        #     subject='Report',
        #     message='We have your filter, go to the site',
        #     from_email='admin@admin.com',
        #     recipient_list=[user.email],
        #     fail_silently=False,
        # )
