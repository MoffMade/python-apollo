import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('deleteSequenceAlteration')
@click.argument("uniquename")


@pass_context
@apollo_exception
@dict_output
def cli(ctx, uniquename):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.deleteSequenceAlteration(uniquename)