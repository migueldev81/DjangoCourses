from django.db import models

class Career(models.Model):
    name = models.CharField(max_length=3)
    code = models.CharField(max_length=35, primary_key=True)
    duration = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.name)
