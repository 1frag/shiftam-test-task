from typing import List

from pydantic import BaseModel

from constants import TRACKED_SMART_CONTRACT
from intergrations.providers.base import BaseWeb3Provider
from shared.types import Event


class GetEventsOutput(BaseModel):
    events: List[Event]


class GetEventsCase:
    def __init__(self, web3: BaseWeb3Provider):
        self.web3 = web3

    async def __call__(self, from_block: int):
        events = await self.web3.get_events(
            contract_address=TRACKED_SMART_CONTRACT,
            from_block=from_block,
            to_block=None,
        )
        return GetEventsOutput(events=events)
