from typing import Sequence
import itertools

from core.clients import DataClient
from core.entities import Data


async def get_data(
        client: DataClient,
        urls: Sequence[str],
) -> list[Data]:
    datas = await client.get_data(urls)
    all_data = [d.get('result', []) for d in datas]
    return list(itertools.chain(*all_data))
