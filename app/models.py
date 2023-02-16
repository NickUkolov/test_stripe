from django.db import models


class Item(models.Model):

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    price = models.IntegerField(default=0)
    currency = models.CharField(max_length=3, blank=True, null=True)
    order = models.ForeignKey('Order', related_name='item', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_display_price(self):
        return f'{self.price/100:.2f}'


class Order(models.Model):

    name = models.CharField(max_length=128, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, default=None)
    paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    # def sum_price(self):
    #     price = []
    #     items = self.item.all()
    #     for item in items:
    #         price.append(int(item.price))
    #     return sum(price)/100


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
