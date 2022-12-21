from unittest.mock import Mock, AsyncMock

import pytest

from usecases.get_balance import GetBalanceCase


@pytest.mark.asyncio
async def test_get_balance():
    mock_web3 = Mock()
    mock_web3.get_balance = AsyncMock()
    mock_web3.get_balance.return_value = 123

    result = await GetBalanceCase(mock_web3)('0xb37a5ba4060d6bfd00a3bfcb235bb596f13932bd', 456)

    assert result == {'balance': 123}
