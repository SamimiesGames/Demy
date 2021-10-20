from typing import Iterable
import click


def progressbar(label: str, iterable: Iterable):
    return click.progressbar(
        iterable, label=label, fill_char="#", empty_char=" ",
        bar_template="%(label)s [%(bar)s] %(info)s"
    )
