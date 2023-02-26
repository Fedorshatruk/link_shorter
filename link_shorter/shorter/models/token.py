from django.db import models


class Token(models.Model):
    owner = models.ForeignKey(
        'shorter.Owner',
        verbose_name='Владелец',
        on_delete=models.CASCADE,
    )
    full_url = models.URLField(verbose_name='ссылка')
    subpart = models.CharField(
        verbose_name='суб домен',
        max_length=20,
        unique=True,
    )
    request_count = models.PositiveIntegerField(
        verbose_name='количество переходов',
        default=0,
    )
    created_date = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'токен'
        verbose_name_plural = 'токены'
