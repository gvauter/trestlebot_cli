"""
Common options for trestle-bot commands.
"""

import functools
import os

import click
import yaml


ENVVAR_PREFIX = "TRESTLEBOT"


def load_config(ctx, param, value):
    """
    Callback for loading config file into Click context.

    Note: This will always run before other options because the --config is_eager is True.
    """
    if os.path.exists(value):
        with open(value, "r") as f:
            _config = yaml.safe_load(f.read())
            if not ctx.default_map:
                ctx.default_map = _config
            else:
                ctx.default_map.update(_config)
        return value
    return None


def common_options(f):
    """
    Configures common options used across commands.
    """

    @click.pass_context
    @click.option(
        "--working-dir",
        type=click.Path(),
        help="Path to root directory of trestle workspace",
        envvar="TRESTLEBOT_WORKING_DIR",
        default=".",
    )
    @click.option(
        "--config",
        "-c",
        type=click.Path(),
        help="Path to trestlebot configuration file",
        envvar="TRESTLEBOT_CONFIG",
        default=".trestlebot/config.yml",
        is_eager=True,
        callback=load_config,
    )
    @functools.wraps(f)
    def wrapper_common_options(*args, **kwargs):
        return f(*args, **kwargs)

    return wrapper_common_options
