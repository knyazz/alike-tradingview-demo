from server.utils import generate_movement


def test_generate_movement():
    assert generate_movement() in (-1, 1)
