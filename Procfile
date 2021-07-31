web: gunicorn --bind :8000 iotd.wsgi:application
celery_worker: celery worker -A iotd -concurrency=1 --loglevel=INFO -n worker.%%h
celery_beat: celery beat -A iotd --scheduler django_celery_beat.schedulers:DatabaseScheduler --loglevel=INFO