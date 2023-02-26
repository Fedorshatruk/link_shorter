from django.db import models


class Owner(models.Model):
    session_id = models.CharField(
        unique=True,
        verbose_name='cессия',
        max_length=30,
    )

    class Meta:
        verbose_name = 'владелец'
        verbose_name_plural = 'владельцы'
