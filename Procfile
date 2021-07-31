celery_worker: celery -A iotd worker -l INFO
celery_beat: celery beat -A iotd --scheduler django_celery_beat.schedulers:DatabaseScheduler --loglevel=INFO