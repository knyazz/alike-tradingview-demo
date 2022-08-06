import collections
import datetime

now: datetime.datetime = datetime.datetime.utcnow().isoformat() + "Z"
connected = set()
tickers: dict = {
    i: {
        "time": now,
        "current": 0,
        "values": collections.deque([
            {
                "time": now,
                "value": 0
            }
        ])
    }
    for i in range(0, 100)
}

TICK: int = 3

WS: dict = {
    'host': '0.0.0.0',
    'port': 5678
}
