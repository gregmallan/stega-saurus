from pathlib import Path

import pytest

from stega import __app_name__, __version__
from stega.cli.command import app

COMMAND = 'textimg'

ENCODE = 'encode'
DECODE = 'decode'


def test_no_sub_command(cli_runner):
    result = cli_runner.invoke(app, [COMMAND, ])
    assert result.exit_code == 2
    assert f'Error: Missing command' in result.stdout


@pytest.fixture
def non_existent_image_path(tmp_path) -> Path:
    int_path = tmp_path.joinpath('doesnotexist.jpg')
    assert int_path.exists() is False
    return int_path


@pytest.fixture
def some_dir_path(tmp_path) -> Path:
    dir = tmp_path.joinpath('somedir')
    dir.mkdir()
    assert dir.exists()
    return dir


@pytest.fixture
def out_image_path(tmp_path) -> Path:
    outpath = tmp_path.joinpath('outimg.png')
    assert outpath.exists() is False
    return outpath


class TestEncodeErr():
    SUB_COMMAND = ENCODE

    def test_no_args(self, cli_runner):
        result = cli_runner.invoke(app, [COMMAND, self.SUB_COMMAND, ])
        assert result.exit_code == 2
        assert f'Error: Missing argument' in result.stdout

    @pytest.mark.parametrize('args', [
        (),
        ('/tmp/testout.png',),
    ])
    def test_missing_args(self, cli_runner, args, original_image_path):
        result = cli_runner.invoke(app, [COMMAND, self.SUB_COMMAND, original_image_path.as_posix(), *args])
        assert result.exit_code == 2
        assert f'Error: Missing argument' in result.stdout

    def test_in_img_path_does_not_exist(self, cli_runner, non_existent_image_path, out_image_path):
        result = cli_runner.invoke(
            app,
            [
                COMMAND,
                self.SUB_COMMAND,
                non_existent_image_path.as_posix(),
                out_image_path.as_posix(),
                'Ahh! The Lopper!',
            ]
        )

        assert result.exit_code == 2
        assert 'does not exist' in result.stdout

    def test_out_img_path_is_dir_not_file(self, cli_runner, original_image_path, some_dir_path):
        result = cli_runner.invoke(
            app,
            [
                COMMAND,
                self.SUB_COMMAND,
                original_image_path.as_posix(),
                some_dir_path.as_posix(),
                'Ahh! The Lopper!',
            ]
        )

        assert result.exit_code == 2
        assert "Invalid value for 'OUT_IMAGE_PATH'" in result.stdout
        assert "is a directory" in result.stdout

    def test_empty_message(self, cli_runner, original_image_path, out_image_path):
        result = cli_runner.invoke(
            app,
            [
                COMMAND,
                self.SUB_COMMAND,
                original_image_path.as_posix(),
                out_image_path.as_posix(),
                '',
            ]
        )

        assert result.exit_code == 2
        assert "Invalid value for 'MSG'" in result.stdout
        assert "Message must not be empty" in result.stdout


class TestEncode():
    SUB_COMMAND = ENCODE

    def test_encode(self, cli_runner, original_image_path, out_image_path):
        result = cli_runner.invoke(
            app,
            [
                COMMAND,
                self.SUB_COMMAND,
                original_image_path.as_posix(),
                out_image_path.as_posix(),
                'Ahh! The Lopper!',
            ]
        )

        assert result.exit_code == 0
        lines = result.stdout.strip().strip('\n').split('\n')
        assert "Decode key: " in lines[-1]
        last_line_parts = lines[-1].split(' ')
        key = last_line_parts[-1].strip()
        assert key == 'bg'

        out_image_path.unlink()  # Don't leave the large png in tmp


class TestDecodeErr():
    SUB_COMMAND = DECODE

    def test_no_args(self, cli_runner):
        result = cli_runner.invoke(app, [COMMAND, self.SUB_COMMAND, ])
        assert result.exit_code == 2
        assert f'Error: Missing argument' in result.stdout

    @pytest.mark.parametrize('args', [
        (),
    ])
    def test_missing_args(self, cli_runner, encoded_image_path, args):
        result = cli_runner.invoke(app, [COMMAND, self.SUB_COMMAND, encoded_image_path.as_posix(), *args])
        assert result.exit_code == 2
        assert f'Error: Missing argument' in result.stdout

    def test_in_img_path_does_not_exist(self, cli_runner, non_existent_image_path):
        result = cli_runner.invoke(
            app,
            [
                COMMAND,
                self.SUB_COMMAND,
                non_existent_image_path.as_posix(),
                'somekey',
            ]
        )

        assert result.exit_code == 2
        assert 'does not exist' in result.stdout

    def test_in_path_is_dir_not_file(self, cli_runner, some_dir_path):
        result = cli_runner.invoke(
            app,
            [
                COMMAND,
                self.SUB_COMMAND,
                some_dir_path.as_posix(),
                'somekey',
            ]
        )

        assert result.exit_code == 2
        assert "Invalid value for 'IN_IMAGE_PATH'" in result.stdout
        assert "is a directory" in result.stdout

    def test_empty_key(self, cli_runner, encoded_image_path):
        result = cli_runner.invoke(
            app,
            [
                COMMAND,
                self.SUB_COMMAND,
                encoded_image_path.as_posix(),
                '',
            ]
        )

        assert result.exit_code == 2
        assert "Invalid value for 'KEY'" in result.stdout
        assert "Key must not be empty" in result.stdout


class TestDecode():
    SUB_COMMAND = DECODE

    def test_encode(self, cli_runner, encoded_image_path):
        result = cli_runner.invoke(
            app,
            [
                COMMAND,
                self.SUB_COMMAND,
                encoded_image_path.as_posix(),
                'bg',
            ]
        )

        assert result.exit_code == 0
        lines = result.stdout.strip().strip('\n').split('\n')
        assert lines[-2] == 'Encoded message:'
        assert lines[-1] == 'Ahh! The Lopper!'
