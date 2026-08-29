import click


@click.command()
def hello():
    click.echo("Hello from the custom Bench CLI!")


commands = [hello]
