import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('show_user')
@click.argument("user", type=str)


@pass_context
@apollo_exception
@dict_output
def cli(ctx, user):
    """Get a specific user
    """
    return ctx.gi.users.show_user(user)