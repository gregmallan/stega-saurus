from pathlib import Path
from shutil import copyfile

from PIL import Image

from image.text import encode, decode

# TODO: Skipping pixels - take from key
EVERY_PX = 100

TEST_IMG = 'skydome.jpg'

OUT_DIR = Path('/tmp', 'stega', 'out')

TEST_MSG = "And if you don't love me now\nYou will never love me again\nI can still hear you saying\nYou would never break the chain (Never break the chain).\n\nTest ûñįçœdë characters"


def main():
    in_img_path = Path.cwd().parent.joinpath('tests', 'integration', '.fixtures', 'img', TEST_IMG)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR.joinpath(f'out-{TEST_IMG}')
    # TODO: check if outpath exists

    with Image.open(in_img_path) as out_image:
        start = out_image.width * 3 - 1  # TODO: Don't use this as the start, take from key.
        every_px = EVERY_PX
        print('ENCODING...')  # TODO: REMOVE - NO COMMIT!!
        print(TEST_MSG)  # TODO: REMOVE - NO COMMIT!!
        encoded_msg_len_str = encode(out_image, TEST_MSG, start=start, every_px=every_px)
        out_image.show()
        out_image.save(out_path)
        print('DECODING... ')  # TODO: REMOVE - NO COMMIT!!
        decoded_msg = decode(out_image, encoded_msg_len_str, start=start, every_px=every_px)
        print(decoded_msg)  # TODO: REMOVE - NO COMMIT!!
        assert TEST_MSG == decoded_msg


if __name__ == '__main__':
    main()
