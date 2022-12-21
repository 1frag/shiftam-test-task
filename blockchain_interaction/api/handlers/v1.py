from fastapi import APIRouter

from intergrations.providers.avalanche import AvalancheProvider
from shared.validation.eth_address import EthAddress
from usecases.get_balance import GetBalanceCase, GetBalanceOutput
from usecases.get_events import GetEventsCase, GetEventsOutput

router = APIRouter()


@router.get('/v1/balance', response_model=GetBalanceOutput)
async def get_balance(block_number: int, wallet_address: EthAddress):
    usecase = GetBalanceCase(
        AvalancheProvider()
    )
    return await usecase(wallet_address, block_number)


@router.get('/v1/events', response_model=GetEventsOutput)
async def get_events(from_block: int):
    usecase = GetEventsCase(
        AvalancheProvider()
    )
    return await usecase(from_block)
