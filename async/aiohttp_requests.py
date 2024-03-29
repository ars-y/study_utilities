import aiohttp
import asyncio

from async_decorators import async_timer
from conf import AMOUNT_REQUESTS, REQUEST_URL


async def get_response_status(session: aiohttp.ClientSession, url: str) -> int:
    """Корутина возвращает статус ответа."""
    async with session.get(url) as response:
        return response.status


@async_timer
async def main() -> None:
    """Асинхронно делаем множество запросов к указанному URL."""
    urls: list = [REQUEST_URL for _ in range(AMOUNT_REQUESTS)]
    async with aiohttp.ClientSession() as session:
        coros: list = [
            get_response_status(session, url)
            for url in urls
        ]

        results: list = await asyncio.gather(*coros)
        print(*results)


if __name__ == '__main__':
    asyncio.run(main())
