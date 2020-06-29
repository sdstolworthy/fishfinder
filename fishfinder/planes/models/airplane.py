from django.db import models
from faker import Faker

fake = Faker()


class Airplane(models.Model):

    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    url = models.TextField(blank=False, null=False, unique=True)
    title = models.TextField(blank=True, null=True)

    @staticmethod
    def faked():
        return Airplane(price=fake.random_int(10000, 25000))

    def __str__(self):
        return "Airplane: {} for ${} at {url}".format(
            self.title, self.price, url=self.url
        )
