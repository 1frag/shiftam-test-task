import logging

from web3 import Web3

from intergrations.providers.base import BaseWeb3Provider
from settings import settings


class AvalancheProvider(BaseWeb3Provider):
    def __init__(self):
        self.provider = Web3(Web3.HTTPProvider(settings.avalanche_rpc))

    async def get_balance(self, wallet_address: str, block_number: int | None):
        logging.info('Getting balance', extra={
            'wallet_address': wallet_address,
            'block_number': block_number,
        })
        balance = self.provider.eth.get_balance(wallet_address, block_number)

        logging.info('Got balance', extra={
            'wallet_address': wallet_address,
            'block_number': block_number,
            'balance': balance,
        })
        return balance

    async def get_events(self, contract_address: str | None, from_block: int | None, to_block: int | None):
        logging.info('Getting events', extra={
            'contract_address': contract_address,
            'from_block': from_block,
            'to_block': to_block,
        })
        events = self.provider.eth.get_logs({
            'address': contract_address,
            'fromBlock': from_block,
            'toBlock': to_block,
        })

        logging.info('Got events', extra={
            'contract_address': contract_address,
            'from_block': from_block,
            'to_block': to_block,
            'events_count': len(events),
        })
        return events
