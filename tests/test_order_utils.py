from __future__ import annotations

from src.order_utils import LineItem, TTLMap, calculate_total, paginate


def test_calculate_total() -> None:
    items = [LineItem(price=10.00, quantity=2)]

    assert calculate_total(items, discount_percent=10, tax_percent=20) == 21.60


def test_paginate() -> None:
    items = [1, 2, 3, 4, 5]

    assert paginate(items, page=1, per_page=2) == [1, 2]
    assert paginate(items, page=3, per_page=2) == [5]


def test_ttl_map_basic() -> None:
    cache = TTLMap(ttl_seconds=60)

    cache.set("a", 123)

    assert cache.get("a") == 123
