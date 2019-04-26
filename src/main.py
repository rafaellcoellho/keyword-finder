import os
import json
from aiohttp import web
from aiohttp_swagger import setup_swagger

routes = web.RouteTableDef()

@routes.post('/')
async def crawler(request):
    req = json.loads(await request.content.read())
    word = req['word']
    links = req['urls']
    
    res = {}
    for link in links:
        res[link] = 0
    
    return web.json_response(res)

@routes.get('/alive')
async def alive(request):
    return web.Response(text="RUNNING")

async def main(): 
  env = os.getenv('APP_ENV')
  print("we are in [{}] mode".format(env))
  app = web.Application()
  app.add_routes(routes)
  if env == 'development':
      setup_swagger(app, swagger_url="/docs", swagger_from_file="docs/main.yaml")
  return app

