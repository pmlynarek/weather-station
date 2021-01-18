from weather.weather import app
from weather.util import sanic_config_manager

from asyncio import get_event_loop, ensure_future


from weather.plugin.opentracing import setup_opentracing

setup_opentracing(app=app)


sanic_config_manager(app, prefix="SANIC_")


if __name__ == "__main__":

    server = app.create_server(host="0.0.0.0", port="8000", return_asyncio_server=True)
    try:
        loop = get_event_loop()
        task = ensure_future(server)
        loop.run_forever()
    except Exception:
        loop.stop()
