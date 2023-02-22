# pyAnyPay

Little asynchronous wrapper around the [AnyPay API](https://anypay.io/doc/api).

## Installation

![PyPI](https://img.shields.io/pypi/v/pyanypay)

```bash
pip install pyanypay
```

## Usage

```python
import asyncio
from pyanypay import AnyPayApi

api = AnyPayApi(api_key="API_KEY", api_id=123)

async def main():
    # Retrieve balance
    response = await api.balance()
    print(response.balance)  # 123.45


asyncio.run(main())
```
