from flask.cli import FlaskGroup
from werkzeug.security import generate_password_hash

from tamriel import alchemy


cli = FlaskGroup(app)


@cli.command("poke")
def poke_flask_app():
    """A test function to check the app is alive."""
    print("===\nUp and running, dude!\n===")


@cli.command("create_db")
def create_db():
    print("create db was called")


@cli.command("seed_db")
def seed_db():
    print("seed db was called")


if __name__ == "__main__":
    cli()
