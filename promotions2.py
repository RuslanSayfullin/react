from decimal import Decimal
import inspect
from strategy import Order
import promotions

promos = [func for _, func in inspect.getmembers(promotions, inspect.isfunction)]


def best_promo(order: Order) -> Decimal:
    """Вычислить наибольшую скидку"""
    return max(promo(order) for promo in promos)
