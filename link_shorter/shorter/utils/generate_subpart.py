import random

from django.utils.baseconv import BASE62_ALPHABET
from django.conf import settings

from shorter.models import Token


def get_random_string() -> str:
    return ''.join(random.choices(BASE62_ALPHABET, k=settings.TOKEN_LENGTH))


def generate_subpart() -> str:
    while True:
        subpart = get_random_string()
        if not Token.objects.filter(subpart=subpart).exists():
            return subpart
