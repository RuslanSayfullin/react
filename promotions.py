from decimal import Decimal
from strategy import Order
from strategy2 import (
    fidelity_promo, bulk_item_promo, large_order_promo
)

promos = [promo for name, promo in globals().items()
            if name.endswith('_promo') and
            name != 'best_promo']


def best_promo(order: Order) -> Decimal:
    """Вычислить наибольшую скидку"""
    return max(promo(order) for promo in promos)
