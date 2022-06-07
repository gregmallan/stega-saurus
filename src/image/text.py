RGB = (0, 1, 2)


def _px_num(i, start, every_px, channel_index):
    return (start + i * every_px) + channel_index


def _xcoord(i, start, every_px, channel_index, image_width):
    return _px_num(i, start, every_px, channel_index) % (image_width)


def _ycoord(i, start, every_px, channel_index, image_width):
    return int(_px_num(i, start, every_px, channel_index) / (image_width))


def _coords(i, start, every_px, image_width):
    # return (x0, y0), (x1, y1), (x2, y2)
    return tuple([
        (_xcoord(i, start, every_px, channel_ind, image_width), _ycoord(i, start, every_px, channel_ind, image_width))
        for channel_ind in RGB
    ])


def _encode_digit_in_channel_val(digit, original_channel_val):
    channel_digits = [char for char in str(original_channel_val).zfill(3)]
    channel_digits[-1] = str(digit)
    channel_val = int(''.join(channel_digits))

    if channel_val > 255:
        channel_val -= 10

    return channel_val


def _decode_digit_from_channel_val(channel_val):
    return channel_val % 10


def encode(image, msg, start, every_px):
    pxa = image.load()
    msg_bytes = msg.encode()
    byte_vals = [b for b in msg_bytes]

    # TODO: CHECK image dims vs msg length and needed encoding size

    for i, val in enumerate(byte_vals):
        coords = _coords(i, start, every_px, image.width)
        pixels = [pxa[x, y] for x, y in coords]
        digits = [d for d in str(val).zfill(3)]

        rgb_ind = i % len(RGB)

        for digit, pixel, pixel_coords in zip(digits, pixels, coords):
            new_channel_val = _encode_digit_in_channel_val(digit, pixel[rgb_ind])
            new_pixel = list(pixel)
            new_pixel[rgb_ind] = new_channel_val
            pxa[pixel_coords[0], pixel_coords[1]] = tuple(new_pixel)

    msg_len = len(byte_vals)

    return msg_len


def decode(image, start, every_px, msg_len):
    byte_vals = []
    pxa = image.load()

    for i in range(msg_len):
        coords = _coords(i, start, every_px, image.width)
        rgb_ind = i % len(RGB)
        digits = [str(_decode_digit_from_channel_val(pxa[x, y][rgb_ind])) for x, y in coords]
        byte_val = int(''.join(digits))
        byte_vals.append(byte_val)

    bytes = bytearray(byte_vals)
    msg = bytes.decode()

    return msg
