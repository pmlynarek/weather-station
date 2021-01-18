from os import environ, path
from sanic import Sanic
from gino.ext.sanic import Gino


def sanic_config_manager(app: Sanic, prefix: str = "SANIC_", env_file="../../.env"):
    for variable, value in environ.items():
        if variable.startswith(prefix):
            _, key = variable.split(prefix, 1)
            app.config[key] = value
    if env_file and path.isfile(env_file):
        try:
            with open(env_file) as fh:
                data = fh.read()
            for line in data.split("\n"):
                var, value = line.split("=")
                var = var.replace(prefix, "")
                app.config[var] = value
        except:
            pass


def setup_database_creation_listener(app: Sanic, database: Gino):
    database.init_app(app)

    @app.listener("after_server_start")
    async def setup_database(app: Sanic, loop):
        await database.gino.create_all()
