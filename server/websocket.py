#!/usr/bin/env python
import asyncio
import datetime
import json
import websockets

from config import TICK, WS, tickers, connected
from utils import generate_movement, DequeEncoder


def get_tickers() -> None:
    """
    update data of tickers
    """
    now: datetime.datetime = datetime.datetime.utcnow().isoformat() + "Z"
    for key in tickers.keys():
        tickers[key]["time"] = now
        current_value = tickers[key]["current"] + generate_movement()
        tickers[key]["current"] = current_value
        tickers[key]["values"].append({
            "time": now,
            "value": current_value
        })


def producer() -> str:
    """
    generate new data to send
    """
    get_tickers()
    now: datetime.datetime = datetime.datetime.utcnow().isoformat() + "Z"
    data: str = json.dumps(
        dict(
            now=now,
            tickers=tickers
        ),
        cls=DequeEncoder
    )
    return data


async def producer_handler(websocket, path) -> None:
    # Register.
    connected.add(websocket)
    try:
        while True:
            await asyncio.sleep(TICK)  # waiting to send new data
            message: str = producer()
            if message:
                await websocket.send(message)
    finally:
        # Unregister.
        connected.remove(websocket)


if __name__ == "__main__":
    # init websocket server
    start_server = websockets.serve(
        producer_handler,
        WS['host'],
        WS['port']
    )

    # TODO: remove depreaction warning for python 3.10: use asyncio.new_event_loop
    loop = asyncio.get_event_loop()

    # run event loop for websocket server
    loop.run_until_complete(start_server)
    loop.run_forever()
