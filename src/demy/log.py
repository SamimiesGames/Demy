import click


def error(message):
    click.secho(f"E: {message}", fg="red")


def warning(message):
    click.secho(f"W: {message}", fg="yellow")


def info(message):
    click.echo(message)
