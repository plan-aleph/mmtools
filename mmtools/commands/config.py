from typing import Optional
import typer
from mmengine.config import Config


app = typer.Typer(
    name="config-tool"
)


@app.command()
def build_config(config: str, output_file: Optional[str] = None):
    return typer.echo(Config.fromfile(config).dump(output_file))


if __name__ == '__main__':
    app()
