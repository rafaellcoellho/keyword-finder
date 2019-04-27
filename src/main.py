from src.env_variables import app_env
from aiohttp import web
from src.spider import get_word_count
import json
import aioredis

if app_env == 'development':
    from aiohttp_swagger import setup_swagger

routes = web.RouteTableDef()

@routes.post('/')
async def crawler(request):
    cache = request.app['redis']
    try:
        req = json.loads(await request.content.read())
        word = req['word']
        links = req['urls']
    except:
        return web.HTTPBadRequest()

    res = {}
    for link in links:
        if await cache.hexists('word_count', link):
            bytes = await cache.hget('word_count', link)
            res[link] = bytes.decode()
        else:
            try:
                res[link] = await get_word_count(word, link)
                await cache.hset('word_count', link, res[link])
            except:
                return web.HTTPBadRequest(reason="invalid url")
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
    redis = await aioredis.create_redis_pool('redis://localhost', minsize=5, maxsize=10, loop=app.loop)
    app['redis'] = redis
    return app
