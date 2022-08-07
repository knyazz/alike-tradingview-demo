import collections
import datetime

now: datetime.datetime = datetime.datetime.utcnow().isoformat() + "Z"
connected = set()  # websocket storage
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

# how often send data
TICK: int = 3

# webspocket server settings
WS: dict = {
    'host': '0.0.0.0',
    'port': 5678
}
