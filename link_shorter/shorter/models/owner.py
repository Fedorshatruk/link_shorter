from django.db import models


class Owner(models.Model):
    session_id = models.UUIDField(
        unique=True,
        verbose_name='cессия',
    )

    class Meta:
        verbose_name = 'владелец'
        verbose_name_plural = 'владельцы'
