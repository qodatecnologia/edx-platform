"""
A trivial task for health checks
"""


from celery.task import task
from django.conf import settings
from edx_django_utils.monitoring import set_code_owner_attribute


@task(routing_key=settings.HEARTBEAT_CELERY_ROUTING_KEY)
@set_code_owner_attribute(__name__)
def sample_task():
    return True
