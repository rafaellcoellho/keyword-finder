from src.main import main
from aiohttp import web

async def test_alive(aiohttp_client, loop):
    app = await main()
    client = await aiohttp_client(app)
    resp = await client.get('/alive')
    assert resp.status == 200
    text = await resp.text()
    assert 'RUNNING' in text

async def test_main(aiohttp_client, loop):
    app = await main()
    client = await aiohttp_client(app)
    resp = await client.post('/', json={'word': 'google','urls': ['https://www.google.com']})
    assert resp.status == 200
    json = await resp.json()
    expected_json = {
        'https://www.google.com': "2"
    }
    assert json == expected_json