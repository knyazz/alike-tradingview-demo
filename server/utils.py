import random


def generate_movement() -> int:
    movement = -1 if random.random() < 0.5 else 1
    return movement
