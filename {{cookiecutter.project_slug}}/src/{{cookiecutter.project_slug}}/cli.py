"""Console script for {{cookiecutter.project_slug}}."""

{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse
{%- endif %}
import sys
{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- endif %}

{% if cookiecutter.use_logging == 'y' %}
import logging
from {{ cookiecutter.project_slug }}.settings import LOGGING_DATE_FORMAT, LOGGING_FORMAT, LOGGING_PATH

FILE_NAME = __name__
logging.basicConfig(level=logging.INFO,
                    datefmt=LOGGING_DATE_FORMAT,
                    format=LOGGING_FORMAT,
                    handlers=[
                        logging.FileHandler(
                            f"{LOGGING_PATH}/{FILE_NAME}.log",
                            encoding=None,
                            delay=False),
                        logging.StreamHandler()
                    ])
logger = logging.getLogger()
{%- endif %}

{% if cookiecutter.command_line_interface|lower == 'click' %}
class Config:
    """Configuration Object"""
CONTEXT = click.make_pass_decorator(Config, ensure=True)

@click.group()
@CONTEXT
def cli(ctx):
    '''
        Console script for {{cookiecutter.project_slug}}.
    '''
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli.cli")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0

@cli.command('command')
@CONTEXT
def remove_dupe(ctx):
    return 0
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
def main():
    """Console script for {{cookiecutter.project_slug}}."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "{{cookiecutter.project_slug}}.cli.main")
    return 0
{%- endif %}


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
