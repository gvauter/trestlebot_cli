"""
Root CLI command.
"""

import click

from cli.commands.autosync import autosync_cmd
from cli.commands.version import version_cmd

EPILOG = "See our docs at https://redhatproductsecurity.github.io/trestle-bot"

CONTEXT_SETTINGS = dict(
    help_option_names=["-h", "--help"], auto_envvar_prefix="TRESTLEBOT"
)


@click.group(
    name="trestlebot",
    context_settings=CONTEXT_SETTINGS,
    epilog=EPILOG,
    help="Trestle-bot CLI",
)
@click.pass_context
def root(ctx):
    """Root command"""


root.add_command(autosync_cmd)
root.add_command(version_cmd)
