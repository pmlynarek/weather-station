from sanic import Sanic
from sanic.response import json
from sanic_openapi import swagger_blueprint, doc
from weather.blueprint.health import health
from weather.model import DATABASE
from weather.blueprint.user import user
from weather.util import setup_database_creation_listener


app = Sanic(__name__)


app.blueprint(swagger_blueprint)

app.blueprint(health)

app.blueprint(user)
setup_database_creation_listener(app, DATABASE)


@app.route("/")
async def default(request):
    return json({"message": "hello Sanic!"})
