from ..click_assets import progressbar
from ..log import error
import os


def discover_path(path):
    if path in os.listdir():
        return path

    return None


def discover_all(*paths):
    err = False

    with progressbar("Discovering Paths", paths) as bar:
        for path in bar:
            if discover_path(path) is None:
                err = True
                break

    if err:
        error(f"Could not find '{path}'.")
        return False

    return True

