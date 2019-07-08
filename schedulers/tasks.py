from celery import shared_task


@shared_task(bind=True)
def print_message(name, *args, **kwargs):
    print(f"Celery is working!! {name}")


