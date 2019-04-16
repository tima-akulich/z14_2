from aiohttp import web, ClientSession

app = web.Application()

async def index(request):
    session = ClientSession()
    response = await session.get('')
    return web.json_response({
        'ping': 'ok',
        'name': request.match_info.get('name')
    })


class OtherView(web.View):
    async def get(self, request):
        pass
    async def post(self, request):
        pass
    async def delete(self, request):
        pass

app.add_routes([
    web.get('/{name}', index, name='index')
])

web.run_app(app)
