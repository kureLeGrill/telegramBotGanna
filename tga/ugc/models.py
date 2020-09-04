from django.db import models


class Profile(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='User ID',
    )
    name = models.TextField(
        verbose_name='User name',
    )

    class Meta:
        verbose_name = 'Profiles'