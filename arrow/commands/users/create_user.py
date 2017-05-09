import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('create_user')
@click.argument("email", type=str)
@click.argument("first_name", type=str)
@click.argument("last_name", type=str)
@click.argument("password", type=str)

@click.option(
    "--role",
    help="User's default role, one of \"admin\" or \"user\"",
    type=str
)
@click.option(
    "--metadata",
    help="User metadata",
    type=str
)

@pass_context
@apollo_exception
@dict_output
def cli(ctx, email, first_name, last_name, password, role="user", metadata={}):
    """Create a new user
    """
    return ctx.gi.users.create_user(email, first_name, last_name, password, role=role, metadata=metadata)