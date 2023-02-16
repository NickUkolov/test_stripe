from django.db import models


class Item(models.Model):

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    price = models.IntegerField(default=0)
    currency = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_display_price(self):
        return f'{self.price/100:.2f}'
