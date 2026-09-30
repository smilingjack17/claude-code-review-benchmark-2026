from __future__ import annotations

from dataclasses import dataclass
from time import monotonic
from typing import Sequence


@dataclass(frozen=True)
class LineItem:
    price: float
    quantity: int


def calculate_total(
    items: Sequence[LineItem],
    discount_percent: float = 0.0,
    tax_percent: float = 18.0,
) -> float:
    subtotal = sum(item.price * item.quantity for item in items)

    discount_amount = subtotal * discount_percent / 100.0
    taxable = subtotal - discount_amount
    tax = taxable * tax_percent / 100.0

    return round(taxable + tax, 2)


def paginate(
    items: Sequence[object],
    page: int,
    per_page: int,
) -> list[object]:
    if page < 1:
        raise ValueError("page must be >= 1")

    if per_page < 1:
        raise ValueError("per_page must be >= 1")

    start = (page - 1) * per_page
    end = start + per_page

    return list(items[start:end])


class TTLMap:
    def __init__(self, ttl_seconds: float) -> None:
        if ttl_seconds <= 0:
            raise ValueError("ttl_seconds must be > 0")

        self._ttl_seconds = ttl_seconds
        self._values: dict[str, tuple[object, float]] = {}

    def set(self, key: str, value: object) -> None:
        self._values[key] = (
            value,
            monotonic() + self._ttl_seconds,
        )

    def get(self, key: str, default: object | None = None) -> object | None:
        entry = self._values.get(key)

        if entry is None:
            return default

        value, expires_at = entry

        if monotonic() >= expires_at:
            del self._values[key]
            return default

        return value
