from hashlib import sha256
from typing import NoReturn, Optional, Union

import aiohttp
import msgspec

from pyanypay.exceptions import AnyPayException
from pyanypay.types import (
    LANG,
    PAYMENT_CURRENCIES,
    PAYMENT_METHODS,
    PAYOUT_COMMISSION_TYPES,
    PAYOUT_TYPES,
    PAYOUT_WALLET_CURRENCIES,
    BalanceResponse,
    BaseResponse,
    BaseResponseError,
    BaseResponseResult,
    CommissionsResponse,
    CreatePaymentResponse,
    CreatePayoutResponse,
    ErrorResponse,
    IPNotificationResponse,
    PaymentsResponse,
    PayoutsResponse,
    RatesResponse,
)


class AnyPayAPI:
    def __init__(self, api_key: str, api_id: int):
        self.api_key: str = api_key
        self.api_id: int = api_id

    async def request(self, path: str, sign: str, **params) -> BaseResponseResult:
        """Make a request to the API."""
        url = f"https://anypay.io/api/{path}/{self.api_id}"
        headers = {
            "Accept": "application/json",
            "Content-Type": "multipart/form-data",
        }
        params["sign"] = sign
        async with aiohttp.ClientSession() as session:
            async with session.request("POST", url, headers=headers, data=params) as response:
                content = await response.read()
        response_obj: BaseResponse = msgspec.json.decode(content, type=BaseResponse)  # type: ignore
        return self.validate_response(response_obj)

    def validate_response(self, response: BaseResponse) -> Union[BaseResponseResult, NoReturn]:
        """Validate the response from the API."""
        if isinstance(response, BaseResponseError):
            obj = msgspec.json.decode(response.error, type=ErrorResponse)
            raise AnyPayException[obj.code](message=obj.message)
        return response

    def generate_sign(self, method: str, *args) -> str:
        """Generate a control signature."""
        params = "".join(str(param) for param in args)
        return sha256(f"{method}{self.api_id}{params}{self.api_key}".encode()).hexdigest()

    async def balance(self) -> BalanceResponse:
        """Get account balance."""
        sign = self.generate_sign("balance")
        response = await self.request("balance", sign)
        return msgspec.json.decode(response.result, type=BalanceResponse)

    async def rates(self) -> RatesResponse:
        """Get rates."""
        sign = self.generate_sign("rates")
        response = await self.request("rates", sign)
        return msgspec.json.decode(response.result, type=RatesResponse)

    async def commisions(self, project_id: int) -> CommissionsResponse:
        """Get commissions."""
        sign = self.generate_sign("commissions", project_id)
        response = await self.request("commissions", sign, project_id=project_id)
        return msgspec.json.decode(response.result, type=CommissionsResponse)

    async def create_payment(
        self,
        project_id: int,
        pay_id: int,
        amount: float,
        currency: PAYMENT_CURRENCIES,
        desc: str,
        method: PAYMENT_METHODS,
        email: str,
        method_currency: Optional[PAYMENT_CURRENCIES] = None,
        phone: Optional[str] = None,
        tail: Optional[str] = None,
        success_url: Optional[str] = None,
        fail_url: Optional[str] = None,
        lang: Optional[LANG] = None,
    ) -> CreatePaymentResponse:
        """Create a payment."""
        sign = self.generate_sign(
            "create-payment", project_id, pay_id, amount, currency, desc, method
        )
        response = await self.request(
            "create-payment",
            sign,
            project_id=project_id,
            pay_id=pay_id,
            amount=amount,
            currency=currency,
            desc=desc,
            method=method,
            email=email,
            method_currency=method_currency,
            phone=phone,
            tail=tail,
            success_url=success_url,
            fail_url=fail_url,
            lang=lang,
        )
        return msgspec.json.decode(response.result, type=CreatePaymentResponse)

    async def payments(
        self,
        project_id: int,
        trans_id: Optional[int] = None,
        pay_id: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> PaymentsResponse:
        """Get payments."""
        sign = self.generate_sign("payments", project_id)
        response = await self.request(
            "payments",
            sign,
            project_id=project_id,
            trans_id=trans_id,
            pay_id=pay_id,
            offset=offset,
        )
        return msgspec.json.decode(response.result, type=PaymentsResponse)

    async def create_payout(
        self,
        payout_id: int,
        payout_type: PAYOUT_TYPES,
        amount: float,
        wallet: str,
        wallet_currency: Optional[PAYOUT_WALLET_CURRENCIES] = None,
        commission_type: Optional[PAYOUT_COMMISSION_TYPES] = None,
        status_url: Optional[str] = None,
    ) -> CreatePayoutResponse:
        """Create a payout."""
        sign = self.generate_sign("create-payout", payout_id, payout_type, amount, wallet)
        response = await self.request(
            "create-payout",
            sign,
            payout_id=payout_id,
            payout_type=payout_type,
            amount=amount,
            wallet=wallet,
            wallet_currency=wallet_currency,
            commission_type=commission_type,
            status_url=status_url,
        )
        return msgspec.json.decode(response.result, type=CreatePayoutResponse)

    async def payouts(
        self,
        trans_id: int,
        payout_id: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> PayoutsResponse:
        """Get payouts."""
        sign = self.generate_sign("payouts")
        response = await self.request(
            "payouts",
            sign,
            trans_id=trans_id,
            payout_id=payout_id,
            offset=offset,
        )
        return msgspec.json.decode(response.result, type=PayoutsResponse)

    async def ip_notification(self) -> IPNotificationResponse:
        """Get IP notification."""
        sign = self.generate_sign("ip-notification")
        response = await self.request("ip-notification", sign)
        return msgspec.json.decode(response.result, type=IPNotificationResponse)
