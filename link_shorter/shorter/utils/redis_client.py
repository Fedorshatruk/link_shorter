import redis
from django.conf import settings

client = redis.Redis(
    **settings.REDIS
)