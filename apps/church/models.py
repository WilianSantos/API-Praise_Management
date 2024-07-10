from django.db import models

from datetime import datetime


class Church(models.Model):
    
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Cult(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    date = models.DateField(default=datetime, blank=False)
    preacher = models.CharField(max_length=50, null=True, blank=True)
    church = models.OneToOneField(
        to=Church,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='church_cult'
    )

    def __str__(self) -> str:
        return self.date
