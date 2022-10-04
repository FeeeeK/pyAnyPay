from typing import Literal

# NOTE: Not all strings have comments because they are self-explanatory.

PAYMENT_CURRENCIES = Literal[
    "RUB",  # Russian ruble
    "UAH",  # Ukrainian hryvnia
    "BYN",  # Belarusian ruble
    "KZT",  # Kazakhstani tenge
    "USD",  # US dollar
    "EUR",  # Euro
]

PAYMENT_METHODS = Literal[
    "qiwi",  # QIWI Wallet
    "ym",  # YooMoney
    "wm",  # WebMoney
    "card",  # Bank card
    "advcash",
    "pm",  # Perfect Money
    "applepay",
    "googlepay",
    "samsungpay",
    "sbp",
    "payeer",
    "btc",  # Bitcoin
    "eth",  # Ethereum
    "bch",  # Bitcoin Cash
    "ltc",  # Litecoin
    "dash",  # Dash
    "zec",  # Zcash
    "doge",  # Dogecoin
    "usdt",  # Tether
    "mts",
    "beeline",
    "megafon",
    "tele2",
    "term",  # Terminal
]


LANG = Literal[
    "ru",  # Russian (default)
    "en",  # English
]

PAYMENT_STATUSES = Literal[
    "paid",  # Payment is successful
    "waiting",  # Waiting for payment
    "refund",
    "canceled",
    "expired",  # Payment lifetime has expired
    "error",
]

PAYOUT_TYPES = Literal[
    "qiwi",  # QIWI Wallet
    "ym",  # YooMoney
    "wm",  # WebMoney
    "mp",  # Mobile phone
    "card",  # Bank card
]

PAYOUT_WALLET_CURRENCIES = Literal[
    "RUB",  # Russian ruble
    "UAH",  # Ukrainian hryvnia
]

PAYOUT_COMMISSION_TYPES = Literal[
    "payment",  # Commission from the payment amount
    "balance",  # Commission from the balance
]

PAYOUT_STATUSES = Literal[
    "paid",  # Payout is successful
    "in_progress",  # Payout is sent to the payment system
    "cancelled",  # Payment system has rejected the payout
    "blocked",  # Monitoring system has blocked the payout
]


ERROR_CODES = Literal[
    "100",  # Incorrect request format
    "101",  # Authentication error
    "102",  # Incorrect control signature
    "103",  # API is disabled for this account
    "104",  # IP address restriction
    "200",  # Incorrect project identifier
    "201",  # Project is inactive
    "202",  # Incorrect payment number.
    "203",  # Incorrect payment amount
    "204",  # Payment amount is lower than the admissible amount
    "205",  # Payment amount is larger than the admissible amount
    "206",  # Payment currency is incorrect
    "207",  # Incorrect payment method
    "208",  # Payment method is not available
    "209",  # The currency of the payment method is incorrect
    "210",  # Payment description not specified
    "211",  # Incorrect email address
    "212",  # Incorrect phone number
    "213",  # Incorrect success url format
    "214",  # Incorrect success url format
    "215",  # Failed to generate payment link
    "300",  # Invalid payment direction
    "301",  # Incorrect beneficiary account number format
    "302",  # Incorrect commission type
    "303",  # Incorrect payment amount
    "304",  # Incorrect payment number
    "305",  # Insufficient funds on balance
    "306",  # Payment amount is less than the allowable amount
    "307",  # Amount of payment is more than admissible
    "308",  # Incorrect status url format
    "309",  # Internal technical error
    "310",  # Operation is prohibited for execution by the user
    "311",  # Payment destination is unavailable
]
