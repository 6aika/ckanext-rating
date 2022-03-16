import click

import ckanext.rating.utils as utils


def get_commands():
    return [rating]


@click.group()
def rating():
    pass


@rating.command()
def init():
    utils.init_db()