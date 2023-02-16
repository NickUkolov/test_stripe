from django.contrib import admin

from app.models import Item, Order

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    fields = ('name', 'description', 'price', 'currency', 'order')

class ItemInline(admin.StackedInline):
    model = Item
    extra = 1


class OrdersAdmin(admin.ModelAdmin):
    # inlines = [ItemInline,]
    fields = ('name', 'paid')

admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrdersAdmin)
