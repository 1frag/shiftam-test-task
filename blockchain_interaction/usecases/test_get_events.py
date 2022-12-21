import json
from unittest.mock import Mock, AsyncMock

import pytest
from hexbytes import HexBytes

from usecases.get_events import GetEventsCase


@pytest.mark.asyncio
async def test_get_events():
    mock_web3 = Mock()
    mock_web3.get_events = AsyncMock()
    mock_logs = [{
        'address': '0x66357dCaCe80431aee0A7507e2E361B7e2402370',
        'blockHash': HexBytes('0x1c53e6249600453b259c344e8e5bb872ae02ef99b6bea8194e104ebb6a1c4c1f'),
        'blockNumber': 23932579,
        'data': '0x000000000000000000000000c7198437980c041c805a1edcba50c1ce5db95118000000000000000000000000b97ef9ef8734c71904d8002f8b6bc66dd9c48a6e000000000000000000000000000000000000000000000000000000003aedbb1d000000000000000000000000000000000000000000000000000000003aebb796',
        'logIndex': 14,
        'removed': False,
        'topics': [
            HexBytes('0x54787c404bb33c88e86f4baf88183a3b0141d0a848e6a9f7a13b66ae3a9b73d1'),
            HexBytes('0x00000000000000000000000073256ec7575d999c360c1eec118ecbefd8da7d12'),
            HexBytes('0x000000000000000000000000db6f1920a889355780af7570773609bd8cb1f498'),
        ],
        'transactionHash': HexBytes('0xbfc5cb8e762d62acab4b1cfef10e150a418ef000c7867e7b7e1699876548ba16'),
        'transactionIndex': 0
    }]
    mock_web3.get_events.return_value = mock_logs

    result = await GetEventsCase(mock_web3)(456)

    assert result == {
        'events': [{
            'address': '0x66357dCaCe80431aee0A7507e2E361B7e2402370',
            'blockHash': '0x1c53e6249600453b259c344e8e5bb872ae02ef99b6bea8194e104ebb6a1c4c1f',
            'blockNumber': 23932579,
            'data': '0x000000000000000000000000c7198437980c041c805a1edcba50c1ce5db95118000000000000000000000000b97ef9ef8734c71904d8002f8b6bc66dd9c48a6e000000000000000000000000000000000000000000000000000000003aedbb1d000000000000000000000000000000000000000000000000000000003aebb796',
            'logIndex': 14,
            'removed': False,
            'topics': [
                '0x54787c404bb33c88e86f4baf88183a3b0141d0a848e6a9f7a13b66ae3a9b73d1',
                '0x00000000000000000000000073256ec7575d999c360c1eec118ecbefd8da7d12',
                '0x000000000000000000000000db6f1920a889355780af7570773609bd8cb1f498',
            ],
            'transactionHash': '0xbfc5cb8e762d62acab4b1cfef10e150a418ef000c7867e7b7e1699876548ba16',
            'transactionIndex': 0
        }]
    }
