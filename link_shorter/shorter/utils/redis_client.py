from django.conf import settings

import redis

client = redis.Redis(
    **settings.REDIS
)
