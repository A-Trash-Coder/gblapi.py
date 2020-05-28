from aiohttp import web
import discord
import asyncio
import socket    

class WebhookServer:
    def __init__(self, bot, secret = None, port: int = 8000, callback: str = "webhook"):
        self.bot = bot
        self.secret = secret
        self.port = port
        self.app = web.Application(loop=bot.loop)
        self.app.add_routes([web.post(f'/{callback}', self.handle_webhook)])
        self.webtask = self.bot.loop.create_task(self.run_server())

    def authorize(self, code):
        if self.secret is None:
            return True
        else:
            return True if code == self.secret else False

    async def run_server(self):
        runner = web.AppRunner(self.app)
        await runner.setup()
        self._webserver = web.TCPSite(runner, '0.0.0.0', self.port)
        await self._webserver.start()
        ip = socket.gethostbyname(socket.gethostname())
        print("----------------------------")
        print(f"Running webhook server at {ip}:{self.port}")
        print("----------------------------")

    async def handle_webhook(self, request):
        data = await request.json()
        x = self.authorize(data["auth"])
        if x is False:
            return
        print(self.bot.dispatch("glenn_vote", data))
        return web.Response(status=200)