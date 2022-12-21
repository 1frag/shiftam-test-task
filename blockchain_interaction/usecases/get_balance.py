from pydantic import BaseModel

from intergrations.providers.base import BaseWeb3Provider


class GetBalanceOutput(BaseModel):
    balance: int


class GetBalanceCase:
    def __init__(self, web3: BaseWeb3Provider):
        self.web3 = web3

    async def __call__(self, wallet_address: str, block_number: int | None):
        balance = await self.web3.get_balance(wallet_address, block_number)
        print(balance)
        return GetBalanceOutput(
            balance=balance,
        )
