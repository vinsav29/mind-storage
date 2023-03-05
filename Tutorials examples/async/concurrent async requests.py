# https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp
import aiohttp
import asyncio
import time
from fastapi import HTTPException
from contextlib import contextmanager
import requests
import httpx

start_time = time.time()


@contextmanager
def request_errors_pass():
    try:
        yield
    except requests.RequestException as e:
        print(f"Fail make request error={e}")
    except Exception as e:
        print(f"While making request, raise unknown error={e}")


# async def get_pokemon(session, url):
#     with request_errors_pass():
#         async with session.get(url) as resp:
#             pokemon = await resp.json()
#             if pokemon['name'] == "charmander":
#                 raise HTTPException(status_code=500, detail="cluster_error")
#             return {url: pokemon['name']}
#
#
# async def main():
#
#     async with aiohttp.ClientSession() as session:
#
#         tasks = []
#         for number in range(1, 10):
#             url = f'https://pokeapi.co/api/v2/pokemon/{number}'
#
#             tasks.append(asyncio.ensure_future(get_pokemon(session, url)))
#             # tasks.append(asyncio.create_task(get_pokemon(session, url)))
#
#         # original_pokemon = await asyncio.gather(*tasks)
#         # for pokemon in original_pokemon:
#         for pokemon in await asyncio.gather(*tasks):
#             if pokemon:
#                 print(pokemon)
#             else:
#                 print("charmander IS FUCKED UP!")

async def main():

    async def get_pokemon(url):
        with request_errors_pass():
            # async with httpx.AsyncClient() as client:
            #     resp = await client.get(url=url)
            #     pokemon = resp.json()
            #     if pokemon['name'] == "charmander":
            #         raise HTTPException(status_code=500, detail="cluster_error")
            #     return {url: pokemon['name']}
            resp = await httpx.AsyncClient().get(url=url)
            pokemon = resp.json()
            if pokemon['name'] == "charmander":
                raise HTTPException(status_code=500, detail="cluster_error")
            return {url: pokemon['name']}

    tasks = []
    for number in range(1, 10):
        url = f'https://pokeapi.co/api/v2/pokemon/{number}'

        tasks.append(asyncio.ensure_future(get_pokemon(url)))
        # tasks.append(asyncio.create_task(get_pokemon(session, url)))

    # original_pokemon = await asyncio.gather(*tasks)
    # for pokemon in original_pokemon:
    for pokemon in await asyncio.gather(*tasks):
        if pokemon:
            print(pokemon)
        else:
            print("charmander IS FUCKED UP!")


asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
