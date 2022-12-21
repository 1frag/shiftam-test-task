from pydantic import BaseModel

from shared.validation.eth_address import EthAddress


class _TestModel(BaseModel):
    address: EthAddress


def test_parse_eth_address_in_lowercase():
    model = _TestModel(address='0xb37a5ba4060d6bfd00a3bfcb235bb596f13932bd')
    assert model.address == '0xB37a5BA4060D6bFD00a3bFCb235Bb596F13932Bd'


def test_parse_eth_address_in_checksum_format():
    model = _TestModel(address='0xB37a5BA4060D6bFD00a3bFCb235Bb596F13932Bd')
    assert model.address == '0xB37a5BA4060D6bFD00a3bFCb235Bb596F13932Bd'
