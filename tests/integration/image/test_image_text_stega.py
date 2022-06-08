import pytest

from src.image.text import encode, decode

IMAGE_WIDTH = 2992
IMAGE_MAX_X = IMAGE_WIDTH - 1


@pytest.fixture(params=[
    'Uncle Leo',
    '  Hello Jerry ',
    'Hello Jerry! ',
    'Ahh! The Lopper!',
    "And if you don't love me now\nYou will never love me again\nI can still hear you saying\nYou would never break the chain (Never break the chain)",
    "Test ûñįçœdë characters",
])
def original_msg(request):
    return request.param


def test_encode_decode_default_start_every_px(original_image, original_msg):
    encoded_msg_len_str = encode(original_image, original_msg)
    msg = decode(original_image, encoded_msg_len_str)
    assert msg == original_msg


@pytest.mark.parametrize('start', [
    0, 1, 2, 100, 101, IMAGE_MAX_X - 1, IMAGE_MAX_X, IMAGE_MAX_X + 1, IMAGE_MAX_X * 2, IMAGE_MAX_X * 100
])
def test_encode_decode_default_every_px(original_image, original_msg, start):
    encoded_msg_len_str = encode(original_image, original_msg, start=start)
    msg = decode(original_image, encoded_msg_len_str, start=start)
    assert msg == original_msg


@pytest.mark.parametrize('every_px', [1, 2, 100, 101, 1000, 1001])
def test_encode_decode_default_start(original_image, original_msg, every_px):
    encoded_msg_len_str = encode(original_image, original_msg, every_px=every_px)
    msg = decode(original_image, encoded_msg_len_str, every_px=every_px)
    assert msg == original_msg


@pytest.mark.parametrize('start', [
    0, 1, 2, 100, 101, IMAGE_MAX_X - 1, IMAGE_MAX_X, IMAGE_MAX_X + 1, IMAGE_MAX_X * 2, IMAGE_MAX_X * 100
])
@pytest.mark.parametrize('every_px', [1, 2, 100, 101, 1000, 1001])
def test_encode_decode(original_image, original_msg, start, every_px):
    encoded_msg_len_str = encode(original_image, original_msg, start=start, every_px=every_px)
    msg = decode(original_image, encoded_msg_len_str, start=start, every_px=every_px)
    assert msg == original_msg
