from celery import shared_task
from django.db.models import F

from shorter.models import Token


@shared_task
def add_count(subpart: str) -> None:
    Token.objects.filter(subpart=subpart).update(request_count=F('request_count') + 1)