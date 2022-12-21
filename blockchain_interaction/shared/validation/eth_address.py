import logging

from pydantic import ConstrainedStr, ValidationError
from web3 import Web3


def to_eth_address(value: str) -> str:
    try:
        return Web3.toChecksumAddress(value)
    except Exception as err:
        logging.warning('Cannot parse address', extra={'address': value, 'error': err})
        print(err)
        raise ValidationError()


class EthAddress(ConstrainedStr):
    @classmethod
    def __get_validators__(cls):
        yield from super().__get_validators__()
        yield to_eth_address
