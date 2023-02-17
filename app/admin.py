from django.contrib import admin

from app.models import Item, Order, OrderItem


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    fields = ('name', 'description', 'price', 'currency')


class ItemInline(admin.StackedInline):
    model = OrderItem
    extra = 2


class OrderAdmin(admin.ModelAdmin):
    inlines = [ItemInline, ]
    fields = ('name', 'paid', 'currency')


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
