import sys
from {{cookiecutter.project_slug}}.cli.commands import main_cli


def run_tool():
    sys.exit(main_cli())
