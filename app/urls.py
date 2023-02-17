from django.urls import path

from .views import ItemDetailView, CheckoutSessionView, CancelView, SuccessView, OrderDetailView, \
    CheckoutOrderSessionView

urlpatterns = [
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item'),
    path('buy/<int:pk>/', CheckoutSessionView.as_view(), name='buy'),

    path('order/<int:pk>/', OrderDetailView.as_view(), name='order'),
    path('buy_order/<int:pk>/', CheckoutOrderSessionView.as_view(), name='buy-order'),

    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
]