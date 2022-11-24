from decimal import Decimal
from strategy import Order
from typing import Optional, Callable, NamedTuple

Promotion = Callable[[Order], Decimal]

promos: list[Promotion] = []


def promotion(promo: Promotion) -> Promotion:
    promos.append(promo)
    return promo


def best_promo(order: Order) -> Decimal:
    """Вычислить наибольшую скидку"""
    return max(promo(order) for promo in promos)


@promotion
def fidelity(order: Order) -> Decimal:
    """5%-ная скидка для заказчиков, имеющих не менее 1000 баллов лояльности"""
    if order.customer.fidelity >= 1000:
        return order.total() * Decimal('0.05')
    return Decimal(0)


@promotion
def bulk_item(order: Order) -> Decimal:
    """10%-ная скидка для каждой позиции LineItem, в которой заказано
        не менее 20 единиц"""
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal('0.1')
        return discount


@promotion
def large_order(order: Order) -> Decimal:
    """7%-ная скидка для заказов, включающих не менее 10 различных позиций"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * Decimal('0.07')
    return Decimal(0)
