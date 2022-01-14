from pathlib import Path

from PIL import Image

import pytest


def pytest_report_header(config):
    return ["PROJECT: stega-saurus", ]


@pytest.fixture
def original_image():
    image_name = 'skydome.jpg'
    in_img_path = Path.cwd().joinpath('tests', 'integration', '.fixtures', 'img', image_name)
    image = Image.open(in_img_path)
    print(image)
    return image
