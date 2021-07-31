from celery import shared_task
@shared_task
def add(x, y):
    print("yes tio!", x + y)
    return x + y