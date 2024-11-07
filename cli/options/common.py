"""
Common options for trestle-bot commands.
"""

import functools
import click


def common_options(f):
    """
    Configures common options used across commands.
    """

    @click.pass_context
    @click.option(
        "--working-dir",
        type=click.Path(),
        help="Path to root directory of trestle workspace",
        default=".",
    )
    @functools.wraps(f)
    def wrapper_common_options(*args, **kwargs):
        return f(*args, **kwargs)

    return wrapper_common_options
