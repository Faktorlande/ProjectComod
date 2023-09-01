from django.db import models

class Workers(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    working_hours_month = models.FloatField()
    holiday_this_month = models.BooleanField(default=False)


    def __str__(self):
        return self.name

