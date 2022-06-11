from pathlib import Path

from shutil import copyfile
from typing import Optional

from PIL import Image
import typer

from image.text import encode, decode

__version__ = '0.0.1a'

app = typer.Typer()
state = {"verbose": False}


def version_callback(value: bool):
    if value:
        typer.echo(f'stega-saurus version: {__version__}')
        raise typer.Exit()


def start_callback(value: int):
    if value < 0:
        raise typer.BadParameter("Must be greater than 0")
    return value


def every_px_callback(value: int):
    if value < 1:
        raise typer.BadParameter("Must be greater than 1")
    return value


@app.callback(help='Stega-saurus image steganography')
def main(verbose: Optional[bool] = typer.Option(False, '-v', '--verbose'),
         version: Optional[bool] = typer.Option(None, '--version', callback=version_callback, is_eager=True)):
    """
    Main method for image steganography.
    """

    if verbose:
        state["verbose"] = True
        typer.secho(f"verbose flag not supported yet", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)


@app.command(name='encode', help="Encode a message using an image")
def img_encode(
    in_image_path: Path = typer.Argument(
        ...,
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        help="Original image path to use in encoding"),
    out_image_path: Path = typer.Argument(
        ...,
        exists=False,
        file_okay=True,
        dir_okay=False,
        writable=True,
        readable=True,
        resolve_path=True,
        help="Output image path to encode the message into"),
    msg: str = typer.Argument(..., help="Message to encode in to the image"),
    # start: Optional[int] = typer.Option(
    #     0, '--start', '-s', callback=start_callback, help="Start encoding at the nth pixel"),
    # every_px: Optional[int] = typer.Option(1, '--every-px', '-p', callback=every_px_callback, show_default=False),
):
    """
    Encode a message into a copy of an image.
    """
    typer.secho(f"stega-saurus text image steganography encode", fg=typer.colors.MAGENTA, bold=True)

    if in_image_path == out_image_path:
        typer.secho(
            f"In and out images paths are the same, this would overwrite the original file",
            fg=typer.colors.RED,
            bold=True,
            err=True
        )
        raise typer.Abort()

    typer.echo(typer.style("Encoding...", fg=typer.colors.CYAN, bold=True))

    with Image.open(in_image_path) as out_image:
        key = encode(out_image, msg)
        # out_image.show()

        # Currently only supporting PNG for output file of encoding
        out_image.save(out_image_path, format='png')

        typer.secho("Done encoding", fg=typer.colors.GREEN, bold=True)
        typer.secho(f"decode key: {key}", fg=typer.colors.CYAN, bold=False)


@app.command(name='decode', help="Decode a message from an image")
def img_decode(
    in_image_path: Path = typer.Argument(
        ...,
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        help="Image path with encoded msg"),
    key: str = typer.Argument(..., help="Image path with encoded msg"),
):
    """
    Decode a message from an image.
    """
    typer.secho(f"stega-saurus text image steganography decode", fg=typer.colors.MAGENTA, bold=True)
    typer.secho("Decoding...", fg=typer.colors.CYAN, bold=True)

    with Image.open(in_image_path) as in_image:
        msg = decode(in_image, key)

        typer.secho("Done decoding", fg=typer.colors.GREEN, bold=True)
        typer.secho("Encoded message:", fg=typer.colors.CYAN, bold=True)
        typer.secho(msg)


if __name__ == '__main__':
    app()
