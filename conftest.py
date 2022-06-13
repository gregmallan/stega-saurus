from pathlib import Path

from PIL import Image

import pytest

from typer.testing import CliRunner


def pytest_report_header(config):
    return ["PROJECT: stega-saurus", ]


@pytest.fixture
def cli_runner():
    return CliRunner()


@pytest.fixture(params=['textimg', ])
def command(request):
    return request.param


# Original input image with

@pytest.fixture
def original_image_name():
    return 'skydome.jpg'


@pytest.fixture
def original_image_path(original_image_name):
    return Path.cwd().joinpath('tests', 'integration', '.fixtures', 'img', original_image_name)


@pytest.fixture
def original_image(original_image_path):
    return Image.open(original_image_path)


# Image with encoded message = 'Ahh! The Lopper!' and decode key = 'bg'

@pytest.fixture
def encoded_image_name():
    return 'encodedskydomeout__key__bg.png'


@pytest.fixture
def encoded_image_path(encoded_image_name):
    return Path.cwd().joinpath('tests', 'integration', '.fixtures', 'img', encoded_image_name)


@pytest.fixture
def encoded_image(encoded_image_path):
    return Image.open(encoded_image_path)
