from .discover import discover_all
from ..log import error
import click
import os


def ensure_startup():
    has_root_dir = discover_all("demy")

    if not has_root_dir:
        return False

    os.chdir("demy")

    startup_possible = discover_all(r"templates", r"styles")
    return startup_possible


class DemyProject:
    def __new__(cls):
        click.secho(f"Attempting to create demyproject.", fg="green")

        if not ensure_startup():
            error(f"Unable to create demyproject.")
            return None

        return super(DemyProject, cls).__new__(cls)

    def __init__(self):
        self.templates = os.listdir("templates")
        click.secho(f"found [{len(self.templates)}] template(s)")
        self.styles = os.listdir("styles")
        click.secho(f"found [{len(self.styles)}] style(s)")

        click.secho(f"Created demyproject successfully.", fg="green")
