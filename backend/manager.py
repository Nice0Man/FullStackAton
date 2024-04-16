# manager.py

import typer
from typing_extensions import Annotated

import uvicorn


cli = typer.Typer()


@cli.command("test")
def test():
    pass


@cli.command("run")
def run_server(
    host: Annotated[str, typer.Option("--host", "-h")] = "127.0.0.1",
    port: Annotated[int, typer.Option("--port", "-p")] = 8000,
    reload: Annotated[bool, typer.Option("--reload", "-r")] = True,
    log_level: Annotated[str, typer.Option("--log-level")] = "debug",
    access_log: Annotated[bool, typer.Option("--access-log")] = True,
) -> None:
    uvicorn.run(
        app="src.api.v1:app",
        reload=reload,
        host=host,
        port=port,
        log_level=log_level,
        access_log=access_log,
    )


if __name__ == "__main__":
    cli()
