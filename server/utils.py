import collections
import json
import random


class DequeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, collections.deque):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


def generate_movement() -> int:
    movement = -1 if random.random() < 0.5 else 1
    return movement
