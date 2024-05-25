import typer

from cccut import __app_name__, __version__, SUCCESS, FILE_ERROR

app = typer.Typer(name=__app_name__)

def _version_callback():
    typer.echo(f"{__app_name__} v{__version__}")
    raise typer.Exit()

@app.command()
def main(
    version:bool = typer.Option(False, '--version', '-v', help="Show the application's version and exit."),
    ) -> None:
    if version:
        _version_callback()

if __name__ == 'main.py':
    app()