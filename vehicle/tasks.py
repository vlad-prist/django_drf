from celery import shared_task
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
