web: gunicorn --bind :8000 iotd.wsgi:application
celery_worker: celery -A iotd worker -l INFO
celery_beat: celery beat --app iotd