from datetime import datetime
from typing import Dict, List, Optional, Union

import msgspec

from .literals import (
    PAYMENT_CURRENCIES,
    PAYMENT_METHODS,
    PAYMENT_STATUSES,
    PAYOUT_COMMISSION_TYPES,
    PAYOUT_STATUSES,
    PAYOUT_TYPES,
)


class BaseResponseError(msgspec.Struct, tag=True):
    error: msgspec.Raw


class BaseResponseResult(msgspec.Struct, tag=True):
    result: msgspec.Raw


BaseResponse = Union[BaseResponseError, BaseResponseResult]


class ErrorResponse(msgspec.Struct):
    """Error model."""

    code: int
    message: str


class BalanceResponse(msgspec.Struct):
    """Response model for balance request."""

    balance: float


class RatesInResponse(msgspec.Struct):
    """Response model for incoming rates request."""

    uah: float
    byn: float
    kzt: float
    usd: float
    eur: float
    btc: float
    eth: float
    bch: float
    ltc: float


class RatesOutResponse(msgspec.Struct):
    """Response model for outgoing rates request."""

    uah: float
    usd: float


class RatesResponse(msgspec.Struct, rename={"in_": "in"}):
    """Response model for rates request."""

    in_: RatesInResponse
    out: RatesOutResponse


class CommissionsResponse(msgspec.Struct):
    """Response model for commission request."""

    qiwi: float
    ym: float
    wm: float
    card: float
    applepay: float
    googlepay: float
    samsungpay: float
    payeer: float
    advcash: float
    pm: float
    btc: float
    eth: float
    bch: float
    ltc: float
    mts: float
    beeline: float
    megafon: float
    tele2: float
    exmo: float
    term: float


class CreatePaymentResponse(msgspec.Struct):
    """Response model for create payment request."""

    transaction_id: int
    pay_id: int
    status: PAYMENT_STATUSES
    payment_url: str


class PaymentsResponseItem(msgspec.Struct):
    """Response model for payments request."""

    transaction_id: int
    pay_id: int
    status: PAYMENT_STATUSES
    method: PAYMENT_METHODS
    amount: float
    currency: PAYMENT_CURRENCIES
    profit: float
    email: str
    desc: str
    date: datetime
    pay_date: Optional[datetime] = None


class PaymentsResponse(msgspec.Struct):
    """Response model for payments request."""

    total: int
    payments: Dict[str, PaymentsResponseItem]


class PayoutsResponseItem(msgspec.Struct):
    """Response model for payouts request."""

    transaction_id: int
    payout_id: int
    payout_type: PAYOUT_TYPES
    status: PAYOUT_STATUSES
    amount: float
    commission: float
    commission_type: PAYOUT_COMMISSION_TYPES
    rate: float
    wallet: int
    date: datetime
    complete_date: Optional[datetime] = None


class PayoutsResponse(msgspec.Struct):
    """Response model for payouts request."""

    total: int
    payouts: Dict[str, PayoutsResponseItem]


class CreatePayoutResponse(PayoutsResponseItem):
    """Response model for create payout request."""

    balance: float = 0.0


class IPNotificationResponse(msgspec.Struct):
    """Response model for IP notification request."""

    ip: List[str]
