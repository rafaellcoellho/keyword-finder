from aiohttp import web

routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    return web.Response(text="Huehue")

async def main(): 
  app = web.Application()
  app.add_routes(routes)
  return app

