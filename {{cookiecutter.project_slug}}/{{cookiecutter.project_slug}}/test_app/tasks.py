from celery import task
from django.utils import timezone


@task()
def task1():
    return 20


@task()
def task1():
    t = timezone.localtime(timezone.now())
    with open('logs.txt', 'a') as f:
        f.write(f"{t}\n")
    return t
