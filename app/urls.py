from django.urls import path

from .views import ItemDetailView, CheckoutSessionView, CancelView, SuccessView

urlpatterns = [
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item'),
    path('buy/<int:pk>/', CheckoutSessionView.as_view(), name='buy'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
]