#!/usr/bin/env python
import asyncio
import datetime
import json
import websockets

from config import TICK, WS
from utils import generate_movement


connected = set()


tickers = {i: 0 for i in range(0, 100)}


def get_tickers() -> None:
    for key in tickers.keys():
        tickers[key] += generate_movement()


def producer() -> str:
    """
    generate new data to send
    """
    now = datetime.datetime.utcnow().isoformat() + "Z"
    get_tickers()
    data = json.dumps(dict(
        now=now,
        tickers=tickers
    ))
    return data


async def producer_handler(websocket, path) -> None:
    # Register.
    connected.add(websocket)
    try:
        while True:
            await asyncio.sleep(TICK)  # this one can be removed
            message = producer()
            if message:
                await websocket.send(message)
    finally:
        # Unregister.
        connected.remove(websocket)


if __name__ == "__main__":
    start_server = websockets.serve(
        producer_handler,
        WS['host'],
        WS['port']
    )

    loop = asyncio.get_event_loop()

    loop.run_until_complete(start_server)
    loop.run_forever()
