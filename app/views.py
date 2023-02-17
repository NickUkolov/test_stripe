import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView, DetailView

from app.models import Item, Order
from app.utils import create_stripe_checkout_session

stripe.api_key = settings.STRIPE_SECRET_KEY


class ItemDetailView(DetailView):
    model = Item
    template_name = 'app/item.html'

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context.update({
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
        })
        return context


class CheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        item = Item.objects.get(id=self.kwargs['pk'])

        checkout_session = create_stripe_checkout_session(obj_name=item.name,
                                                          obj_price=item.price,
                                                          obj_currency=item.currency)
        return JsonResponse({'id': checkout_session.id})


class OrderDetailView(DetailView):
    model = Order
    template_name = 'app/order.html'

    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        context.update({
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
        })
        return context


class CheckoutOrderSessionView(View):
    def get(self, request, *args, **kwargs):
        order = Order.objects.get(id=self.kwargs['pk'])

        checkout_session = create_stripe_checkout_session(obj_name=order.name,
                                                          obj_currency=order.currency,
                                                          obj_price=order.price())
        return JsonResponse({'id': checkout_session.id})


class SuccessView(TemplateView):
    template_name = 'app/success.html'


class CancelView(TemplateView):
    template_name = 'app/cancel.html'
