from django.db import models

from datetime import date


class Church(models.Model):
    
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Cult(models.Model):
    theme = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(default=date.today, blank=False)
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
    

class Function(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    church = models.OneToOneField(
        to=Church,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='fuction_church'
    )

    def __str__(self) -> str:
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    function = models.ManyToManyField(Function)
    availability = models.BooleanField(default=True)
    cell_phone = models.CharField(max_length=14)
    is_member = models.BooleanField(default=False)
    church = models.OneToOneField(
        to=Church,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='member_church'
    )

    def __str__(self) -> str:
        return self.name
