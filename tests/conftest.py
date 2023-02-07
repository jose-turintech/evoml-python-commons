"""
This module contains the configuration and fixtures for the project
services.

Session and test running activities will invoke all hooks defined in
conftest.py files closer to the root of the filesystem.
"""
# pylint: disable=W0613
#        W0613: Unused argument 'exitstatus' (unused-argument)
# ───────────────────────────────────────────────────── imports ────────────────────────────────────────────────────── #
import os

import pytest


# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #
#                                           Update environment configuration                                           #
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #


@pytest.fixture(scope="session", autouse=True)
def set_env_configuration(request):
    """Update the environment configuration for all the tests"""


# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #
#                                          Global testing constants and Types                                          #
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #


# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #
#                                           Fixtures accessible by all tests                                           #
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #


# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #
#                         To see list of deselected tests and their node ids in pytest output                          #
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #

# https://stackoverflow.com/questions/61022267/
# would-like-to-see-list-of-deselected-tests-and-their-node-ids-in-pytest-output


def _pytest_deselected(items):
    """pytest has a hookspec pytest_deselected for accessing the
    deselected tests.
    Example: add this code to conftest.py in your test root dir

    Running the tests now will give you an output similar to this:
        $ pytest -vv
        ...
        plugins: cov-2.8.1, asyncio-0.10.0
        collecting ...
        deselected: test_spam.py::test_spam
        deselected: test_spam.py::test_bacon
        deselected: test_spam.py::test_ham
        collected 4 items / 3 deselected / 1 selected
    """
    if not items:
        return
    config = items[0].session.config
    reporter = config.pluginmanager.getplugin("terminalreporter")
    reporter.ensure_newline()
    for item in items:
        reporter.line(f"deselected: {item.nodeid}", yellow=True, bold=True)


def pytest_deselected(items):
    """If you want a report in another format, simply store the
    deselected items in the config and use them for the desired output
    somewhere else, e.g. pytest_terminal_summary
    """
    if not items:
        return
    config = items[0].session.config
    config.deselected = items


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """
    gives the output:
        $ pytest -vv
        ...
        plugins: cov-2.8.1, asyncio-0.10.0
        collected 4 items / 3 deselected / 1 selected

        ...

        ---------------------- Deselected tests ----------------------
        test_spam.py::test_spam
        test_spam.py::test_bacon
        test_spam.py::test_ham
        ============== 1 passed, 3 deselected in 0.01s ===============
    """
    reports = terminalreporter.getreports("")
    content = os.linesep.join(text for report in reports for secname, text in report.sections)
    deselected = getattr(config, "deselected", [])
    if deselected:
        terminalreporter.ensure_newline()
        terminalreporter.section("Deselected tests", sep="-", yellow=True, bold=True)
        content = os.linesep.join(item.nodeid for item in deselected)
        terminalreporter.line(content)
