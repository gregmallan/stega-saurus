R, G, B = 0, 1, 2

RGB = (R, G, B)


def xcoord(i, start, every_px, image_width):
    return ((i * every_px) + start + every_px) % (image_width)


def ycoord(i, start, every_px, image_width):
    return int(((i - start) * every_px + i) / image_width)


def encode(image, msg, start, every_px):
    pxa = image.load()
    msg_bytes = msg.encode()
    byte_vals = [b for b in msg_bytes]

    # TODO: CHECK image dims vs msg length and needed encoding size

    stop = 0
    for i, val in enumerate(byte_vals, start=start):
        x = xcoord(i, start, every_px, image.width)
        y = ycoord(i, start, every_px, image.width)

        rgb_ind = i % len(RGB)
        px = pxa[x, y]
        r, g, b = px

        new_r = val if rgb_ind == R else r
        new_g = val if rgb_ind == G else g
        new_b = val if rgb_ind == B else b

        new_px = [int(v) for v in [new_r, new_g, new_b]]

        intensity = sum(px)
        new_intensity = sum(new_px)

        # A little extra obfuscation to keep the pixel intensity (brightness) the similar.
        diff = new_intensity - intensity
        # Close enough, don't care about losing a single intensity val for odd remaining
        channel_change = int(diff / 2)

        for j in range(len(RGB)):
            if j != rgb_ind:
                new_px[j] = new_px[j] - channel_change

        new_px = tuple(new_px)
        pxa[x, y] = new_px

        stop = i

    return stop - start


def decode(image, start, every_px, msg_len):
    byte_vals = []
    pxa = image.load()

    for i in range(msg_len + 1):
        ind = start + i
        x = xcoord(ind, start, every_px, image.width)
        y = ycoord(ind, start, every_px, image.width)

        px = pxa[x, y]
        rgb_ind = ind % len(RGB)
        byte_val = px[rgb_ind]
        byte_vals.append(byte_val)

    bytes = bytearray(byte_vals)
    msg = bytes.decode()

    return msg
