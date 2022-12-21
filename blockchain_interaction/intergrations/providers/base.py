from abc import ABC


class BaseWeb3Provider(ABC):
    async def get_balance(self, wallet_address: str, block_number: int | None):
        raise NotImplementedError()

    async def get_events(self, contract_address: str | None, from_block: int | None, to_block: int | None):
        raise NotImplementedError()
