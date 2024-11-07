"""
Module for autosync command.
"""

import click

from cli.options.common import common_options


@click.command(name="autosync", help="Sync markdown changes into OSCAL")
@common_options
def autosync_cmd(ctx, **options):
    """autosync command"""

    working_dir = options.get("working_dir")

    click.echo(f"Running autosync in {working_dir} directory...")
