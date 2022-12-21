from typing import List

from hexbytes import HexBytes
from pydantic import BaseModel, ConstrainedStr

from shared.validation.eth_address import EthAddress


def hex_bytes_to_string(hex_bytes: HexBytes | str) -> str:
    if isinstance(hex_bytes, HexBytes):
        return hex_bytes.hex()
    else:
        return hex_bytes


class HexString(ConstrainedStr):
    @classmethod
    def __get_validators__(cls):
        yield hex_bytes_to_string
        yield from super().__get_validators__()


class Event(BaseModel):
    address: EthAddress
    blockHash: HexString
    blockNumber: int
    data: str | None
    logIndex: int
    removed: bool
    topics: List[HexString]
    transactionHash: HexString
    transactionIndex: int
