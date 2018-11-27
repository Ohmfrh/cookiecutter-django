from celery import task


@task()
def task1():
    return 20
