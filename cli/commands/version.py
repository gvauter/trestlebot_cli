"""
Module for version command
"""

import click


@click.command(name="version", help="Show Trestle-bot CLI version")
@click.pass_context
def version_cmd(ctx):
    """version command"""

    click.echo("trestle-bot: v0.0")
