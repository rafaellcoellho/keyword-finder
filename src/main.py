import os
from aiohttp import web
from aiohttp_swagger import setup_swagger

routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    return web.Response(text="Huehue")

@routes.get('/alive')
async def alive(request):
    """
    ---
    description: This end-point allow to test that service is up.
    tags:
    - Health check
    produces:
    - text/plain
    responses:
        "200":
            description: successful operation. Return "RUNNING" text
        "405":
            description: invalid HTTP Method
    """
    return web.Response(text="RUNNING")

async def main(): 
  env = os.getenv('APP_ENV')
  print("we are in [{}] mode".format(env))
  app = web.Application()
  app.add_routes(routes)
  if env == 'development':
      setup_swagger(app, swagger_url="/docs")
  return app

