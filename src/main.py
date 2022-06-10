from pathlib import Path
from shutil import copyfile

from PIL import Image

from image.text import encode, decode

# TODO: Skipping pixels - take from key
EVERY_PX = 100
TEST_IMG_NAME = 'skydome'
TEST_IMG = f'{TEST_IMG_NAME}.jpg'

OUT_IMG = f'out-{TEST_IMG_NAME}.png'

OUT_DIR = Path('/Users', 'greg', 'Desktop')

TEST_MSG = "And if you don't love me now\nYou will never love me again\nI can still hear you saying\nYou would never break the chain (Never break the chain).\n\nTest ûñįçœdë characters"


def main():
    in_img_path = Path.cwd().parent.joinpath('tests', 'integration', '.fixtures', 'img', TEST_IMG)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR.joinpath(f'{OUT_IMG}')

    with Image.open(in_img_path) as out_image:
        print('ENCODING...')  # TODO: REMOVE - NO COMMIT!!
        print(TEST_MSG)  # TODO: REMOVE - NO COMMIT!!
        encoded_msg_len_str = encode(out_image, TEST_MSG)
        out_image.show()
        # Currently only supporting PNG for output file of encoding
        out_image.save(out_path, format='png')

    with Image.open(out_path) as new_out_img:
        new_out_img.show()  # TODO: REMOVE - NO COMMIT!!
        print('DECODING... ')  # TODO: REMOVE - NO COMMIT!!
        decoded_msg = decode(new_out_img, encoded_msg_len_str)
        print(decoded_msg)  # TODO: REMOVE - NO COMMIT!!
        assert TEST_MSG == decoded_msg


if __name__ == '__main__':
    main()
