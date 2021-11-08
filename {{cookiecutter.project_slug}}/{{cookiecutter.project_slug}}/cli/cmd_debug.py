import click

@click.group(name='debug')
def cli():
    """ Debug One Option Experiment """
    pass

@cli.command()
@click.option('-c', '--cfg-id', required=True)
@click.option('-s', '--symbol', required=True)
@click.option('-d', '--trade-date', required=True, type=click.DateTime(formats=["%Y-%m-%d"]))
@click.option('-p', '--path', required=True, type=click.Path(resolve_path=True))
def x01_preprocess_option(cfg_id, symbol, trade_date, path):
    pass

