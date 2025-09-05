from django.db import models

class Grocery(models.Model):
    name = models.CharField(max_length = 100)
    price = models.IntegerField()
    rating = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

    @classmethod
    def filter(cls, param, name):
        pass
