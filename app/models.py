from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.CharField(max_length=256, verbose_name='Описание')
    price = models.IntegerField(default=0, verbose_name='Цена в центах')
    currency = models.CharField(choices=(('usd', 'usd'),), max_length=3,
                                blank=True, null=True, verbose_name='Валюта')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_display_price(self):
        return f'{self.price / 100:.2f}'


class Order(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False, verbose_name='Оплачено')
    currency = models.CharField(choices=(('usd', 'usd'),), max_length=3,
                                blank=True, null=True, default='usd', verbose_name='Валюта')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def total_price(self):
        return sum([
            order_item.total()
            for order_item in OrderItem.objects.filter(order=self)
        ])

    def price(self):
        return int(self.total_price() * 100)

    def __str__(self):
        return f'{self.name}, ${self.total_price()}: {self.paid}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

    def total(self):
        return (self.count * self.item.price) / 100

    def __str__(self):
        return f'{self.item.name}, ' \
               f'${self.item.price/100} * {self.count} = ${self.total()}'
