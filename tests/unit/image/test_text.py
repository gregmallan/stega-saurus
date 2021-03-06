import pytest

from stega.image.text import _decode_digit_from_channel_val, _encode_digit_in_channel_val


@pytest.mark.parametrize('digit,orig_channel_val,expected_channel_val', [
    (0, 0, 0),
    (1, 0, 1),
    (2, 0, 2),
    (4, 0, 4),
    (5, 0, 5),
    (8, 0, 8),
    (9, 0, 9),

    (0, 1, 0),
    (1, 1, 1),
    (2, 1, 2),
    (4, 1, 4),
    (5, 1, 5),
    (8, 1, 8),
    (9, 1, 9),

    (0, 25, 20),
    (1, 25, 21),
    (2, 25, 22),
    (4, 25, 24),
    (5, 25, 25),
    (8, 25, 28),
    (9, 25, 29),

    (0, 99, 90),
    (1, 99, 91),
    (2, 99, 92),
    (4, 99, 94),
    (5, 99, 95),
    (8, 99, 98),
    (9, 99, 99),

    (0, 100, 100),
    (1, 100, 101),
    (2, 100, 102),
    (4, 100, 104),
    (5, 100, 105),
    (8, 100, 108),
    (9, 100, 109),

    (0, 101, 100),
    (1, 101, 101),
    (2, 101, 102),
    (4, 101, 104),
    (5, 101, 105),
    (8, 101, 108),
    (9, 101, 109),

    (0, 171, 170),
    (1, 171, 171),
    (2, 171, 172),
    (4, 171, 174),
    (5, 171, 175),
    (8, 171, 178),
    (9, 171, 179),

    (0, 249, 240),
    (1, 249, 241),
    (2, 249, 242),
    (4, 249, 244),
    (5, 249, 245),
    (8, 249, 248),
    (9, 249, 249),

    (0, 250, 250),
    (1, 250, 251),
    (2, 250, 252),
    (4, 250, 254),
    (5, 250, 255),
    (6, 250, 246),
    (8, 250, 248),
    (9, 250, 249),

    (0, 251, 250),
    (1, 251, 251),
    (2, 251, 252),
    (4, 251, 254),
    (5, 251, 255),
    (6, 251, 246),
    (8, 251, 248),
    (9, 251, 249),

    (0, 255, 250),
    (1, 255, 251),
    (2, 255, 252),
    (4, 255, 254),
    (5, 255, 255),
    (6, 255, 246),
    (8, 255, 248),
    (9, 255, 249),

])
def test_encode_digit_in_channel_val(digit, orig_channel_val, expected_channel_val):
    result = _encode_digit_in_channel_val(str(digit), orig_channel_val)
    assert result == expected_channel_val


@pytest.mark.parametrize('channel_val,expected_digit', [
    (0, 0),
    (1, 1),
    (2, 2),
    (4, 4),
    (5, 5),
    (8, 8),
    (9, 9),

    (0, 0),
    (1, 1),
    (2, 2),
    (4, 4),
    (5, 5),
    (8, 8),
    (9, 9),

    (20, 0),
    (21, 1),
    (22, 2),
    (24, 4),
    (25, 5),
    (28, 8),
    (29, 9),

    (90, 0),
    (91, 1),
    (92, 2),
    (94, 4),
    (95, 5),
    (98, 8),
    (99, 9),

    (100, 0),
    (101, 1),
    (102, 2),
    (104, 4),
    (105, 5),
    (108, 8),
    (109, 9),

    (100, 0),
    (101, 1),
    (102, 2),
    (104, 4),
    (105, 5),
    (108, 8),
    (109, 9),

    (170, 0),
    (171, 1),
    (172, 2),
    (174, 4),
    (175, 5),
    (178, 8),
    (179, 9),

    (240, 0),
    (241, 1),
    (242, 2),
    (244, 4),
    (245, 5),
    (248, 8),
    (249, 9),

    (250, 0),
    (251, 1),
    (252, 2),
    (254, 4),
    (255, 5),
    (246, 6),
    (248, 8),
    (249, 9),

    (250, 0),
    (251, 1),
    (252, 2),
    (254, 4),
    (255, 5),
    (246, 6),
    (248, 8),
    (249, 9),

    (250, 0),
    (251, 1),
    (252, 2),
    (254, 4),
    (255, 5),
    (246, 6),
    (248, 8),
    (249, 9),

])
def test_decode_digit_from_channel_val(channel_val, expected_digit):
    digit = _decode_digit_from_channel_val(channel_val)
    assert digit == expected_digit
