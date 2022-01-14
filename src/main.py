from pathlib import Path
from shutil import copyfile

from PIL import Image

from image.text import encode, decode

# TODO: Skipping pixels - take from key
EVERY_PX = 100

TEST_IMG = 'skydome.jpg'

OUT_DIR = Path('/tmp', 'stega', 'out')

TEST_MSG = "Master of puppets, he's pulling your strings, twisting your mind and smashing your dreams"

# KEY = 'secret' # TODO: Use key


def main():
    in_img_path = Path.cwd().parent.joinpath('tests', 'integration', '.fixtures', 'img', TEST_IMG)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR.joinpath(f'out-{TEST_IMG}')

    with Image.open(in_img_path) as out_image:
        start = out_image.width * 3 - 1  # TODO: Don't use this as the start, take from key.
        every_px = EVERY_PX
        print('ENCODING...')  # TODO: REMOVE - NO COMMIT!!
        print(TEST_MSG)  # TODO: REMOVE - NO COMMIT!!
        msg_len = encode(out_image, TEST_MSG, start, every_px)
        out_image.show()
        out_image.save(out_path)
        print('DECODING... ')  # TODO: REMOVE - NO COMMIT!!
        decoded_msg = decode(out_image, start, every_px, msg_len)
        print(decoded_msg)  # TODO: REMOVE - NO COMMIT!!
        assert TEST_MSG == decoded_msg


if __name__ == '__main__':
    main()
