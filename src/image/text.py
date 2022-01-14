RGB = (0, 1, 2)


def _xcoord(i, start, every_px, image_width):
    return ((i * every_px) + start + every_px) % (image_width)


def _ycoord(i, start, every_px, image_width):
    return int(((i - start) * every_px + i) / image_width)


def _coords(i, start, every_px, image_width):
    x0 = _xcoord(i, start, every_px, image_width)
    x1 = (x0 + 1) % image_width
    x2 = (x1 + 1) % image_width
    y0 = _ycoord(i, start, every_px, image_width)
    # Do we need to bump to the next row of the image?
    y1 = y0 + 1 if x1 < x0 else y0
    y2 = y1 + 1 if x2 < x1 else y1

    return (x0, y0), (x1, y1), (x2, y2)


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

    stop = 0
    for i, val in enumerate(byte_vals, start=start):
        coords = _coords(i, start, every_px, image.width)
        pixels = [pxa[x, y] for x, y in coords]
        digits = [d for d in str(val).zfill(3)]

        rgb_ind = i % len(RGB)

        for digit, pixel, pixel_coords in zip(digits, pixels, coords):
            new_channel_val = _encode_digit_in_channel_val(digit, pixel[rgb_ind])
            new_pixel = list(pixel)
            new_pixel[rgb_ind] = new_channel_val
            pxa[pixel_coords[0], pixel_coords[1]] = tuple(new_pixel)

        stop = i

    return stop - start


def decode(image, start, every_px, msg_len):
    byte_vals = []
    pxa = image.load()

    for i in range(msg_len + 1):
        ind = start + i
        coords = _coords(ind, start, every_px, image.width)
        rgb_ind = ind % len(RGB)
        digits = [str(_decode_digit_from_channel_val(pxa[x, y][rgb_ind])) for x, y in coords]
        byte_val = int(''.join(digits))
        byte_vals.append(byte_val)

    bytes = bytearray(byte_vals)
    msg = bytes.decode()

    return msg
