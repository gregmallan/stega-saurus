import pytest

from src.image.text import encode, decode

IMAGE_WIDTH = 2992
IMAGE_MAX_X = IMAGE_WIDTH - 1


@pytest.mark.parametrize('start', [
    0, 1, 2, 100, 101, IMAGE_MAX_X - 1, IMAGE_MAX_X, IMAGE_MAX_X + 1, IMAGE_MAX_X * 2, IMAGE_MAX_X * 100
])
@pytest.mark.parametrize('every_px', [1, 2, 100, 101, 1000, 1001])
@pytest.mark.parametrize('original_msg', [
    'Uncle Leo',
    'Hello Jerry',
    '  Hello Jerry ',
    'Hello Jerry! ',
    'Ahh! The Lopper!',
    'Ahhhh!!!! The Lopper!!',
    "Master of puppets, he's pulling your strings, twisting your mind and smashing your dreams blinded by me you can't "
    "see a thing",
    "Master of puppets, he's pulling your strings, twisting your mind and smashing your dreams.",
    "Test ûñįçœdë characters",
    "Master of puppets, he's pulling your strings, twisting your mind and smashing your dreams. Test ûñįçœdë characters"
])
def test_encode_decode(original_image, original_msg, start, every_px):
    msg_len = encode(original_image, original_msg, start, every_px)
    msg = decode(original_image, start, every_px, msg_len)
    assert msg == original_msg
