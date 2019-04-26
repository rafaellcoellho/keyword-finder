from src.env_variables import app_env
from aiohttp import web
import json

if app_env == 'development':
    from aiohttp_swagger import setup_swagger

routes = web.RouteTableDef()

@routes.post('/')
async def crawler(request):
    req = json.loads(await request.content.read())

    try:
        word = req['word']
        links = req['urls']
    except:
        return web.HTTPBadRequest(reason="word or urls parameter not found!")

    res = {}
    for link in links:
        res[link] = 0
    
    return web.json_response(res)

@routes.get('/alive')
async def alive(request):
    return web.Response(text="RUNNING")

async def main(): 
    print("we are in [{}] mode".format(app_env))
    app = web.Application()
    app.add_routes(routes)
    if app_env == 'development':
        setup_swagger(
          app, 
          swagger_url="/docs", 
          swagger_from_file="docs/main.yaml"
        )
    return app

