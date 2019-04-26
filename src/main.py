import os
import json
from aiohttp import web
from aiohttp_swagger import setup_swagger

routes = web.RouteTableDef()

@routes.post('/')
async def crawler(request):
    """
    ---
    description: Conta o número de ocorrencias de uma palavra em urls
    tags:
    - Crawler
    produces:
    - application/json
    responses:
        "200":
            description: Sucesso. Retorna json com os resultados
        "405":
            description: Método Http inválido
        "500":
            description: Erro interno
    """
    req = json.loads(await request.content.read())
    word = req['word']
    links = req['urls']
    print(word, "\n",links)
    return web.Response(text="Huehue")

@routes.get('/alive')
async def alive(request):
    """
    ---
    description: Testar se o serviço está funcionando
    tags:
    - Testes
    produces:
    - text/plain
    responses:
        "200":
            description: Está funcionando. Retorna "RUNNING"
        "405":
            description: Método Http inválido
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

