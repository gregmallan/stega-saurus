from stega import __app_name__, __version__
from stega.cli.command import app


def test_version(cli_runner):
    result = cli_runner.invoke(app, ['--version'])
    assert result.exit_code == 0
    assert f'{__app_name__} version: {__version__}' in result.stdout


def test_version_commands(cli_runner, command):
    result = cli_runner.invoke(app, ['--version', command])
    assert result.exit_code == 0
    assert f'{__app_name__} version: {__version__}' in result.stdout


def test_commands_version(cli_runner, command):
    result = cli_runner.invoke(app, [command, '--version'])
    assert result.exit_code == 0
    assert f'{__app_name__} version: {__version__}' in result.stdout
