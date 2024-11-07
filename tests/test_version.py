"""
Unit test for version command.
"""

import pytest
from click.testing import CliRunner

from cli.commands.version import version_cmd


def test_version():
    runner = CliRunner()

    res = runner.invoke(version_cmd)
    assert res.exit_code == 0
    assert "trestle-bot: v0.0" in res.output
