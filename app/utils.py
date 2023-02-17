import stripe


def create_stripe_checkout_session(obj_name, obj_price, obj_currency):
    domain = 'http://127.0.0.1:8000'

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': obj_currency,
                    'unit_amount': obj_price,
                    'product_data': {
                        'name': obj_name,
                    },
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=domain + '/success/',
        cancel_url=domain + '/cancel/',
    )
    return session
