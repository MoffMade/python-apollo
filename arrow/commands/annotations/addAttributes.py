import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('addAttributes')
@click.argument("feature_id")
@click.argument("attributes")


@pass_context
@apollo_exception
@dict_output
def cli(ctx, feature_id, attributes):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.addAttributes(feature_id, attributes)