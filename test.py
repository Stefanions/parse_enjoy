import httpx
from fake_useragent import UserAgent
import random
from datetime import datetime, time, timedelta
import asyncio
import itertools
# from httpx_parse.proxy_old import *
import json
from config import *
from stealth_requests import AsyncStealthSession
ua = UserAgent()  

# head = {
#     'Accept': 'application/json, text/plain, */*',
#     'Accept-Language': 'en-US,en;q=0.9',
#     'Cache-Control': 'no-cache',
#     'Pragma': 'no-cache',
#     'Referer': 'https://fedresurs.ru/entities',
#     'Sec-Ch-Ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
#     'Sec-Ch-Ua-Mobile': '?0',
#     'Sec-Ch-Ua-Platform': '"Windows"',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
# }

head = {
    "User-Agent": ua.random,
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://fedresurs.ru/entities",
    "Origin": "https://fedresurs.ru"
}

params = {
    "limit": 15,
    "offset": 0,
    "isActive": "true"
}

proxy = "http://BJrr0t:AZu3Ry@94.127.140.200:8000"
async def main():
    # async with AsyncStealthSession(impersonate='safari', proxy=proxy) as session:
    #     response = await session.get("https://fedresurs.ru/backend/companies", params=params, headers=head)
    #     print(response.status_code)
    #     print(response.text)


    async with httpx.AsyncClient(proxy=proxy) as client:
        response = await client.get("https://fedresurs.ru/backend/companies", params=params, headers=head)
        print(response.status_code)
        print(response.text)
    # async with httpx.AsyncClient(proxy=proxy) as client:
    #     response = await client.get("http://httpbin.org/ip")
    #     print(response.json())

# Запуск асинхронной функции
asyncio.run(main())
