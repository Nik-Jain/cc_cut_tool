import typer

from cccut import __app_name__, __version__, SUCCESS, FILE_ERROR

app = typer.Typer(name=__app_name__)

def _version_callback():
    typer.echo(f"{__app_name__} v{__version__}")
    raise typer.Exit()

@app.command()
def main(
    file: typer.FileText = typer.Argument(default=None),
    version: bool = typer.Option(False, '--version', '-v', help="Show the application's version and exit."),
    fields: str = typer.Option(None, '-f', help='Fields to extract')
    ) -> None:
    if version:
        _version_callback()
        return typer.Exit()
    if fields:
        field_indices = [int(i) - 1 for i in fields]
        for line in file:
            parts = line.strip().split('\t')
            selected_parts = [parts[i] for i in field_indices if i < len(parts)]
            print('\t'.join(selected_parts))
if __name__ == 'main.py':
    app()