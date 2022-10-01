import sanic
import aiohttp
import os
import sys
import json

app = sanic.Sanic(__name__)

LINE_NOTIFY_URL = "https://notify-api.line.me/api/notify"

SETTING = json.load(open("secret.json", "r"))
TOKEN = SETTING["line_token"]
DISCORD_WEBHOOK_URL = SETTING["discord_webhook"]


@app.route("/")
async def main_root(request: sanic.Request):
    return sanic.response.json({"Service":"Available"})

@app.route("/line")
async def line_notify(request: sanic.Request):
    if request.args.get("message") is None:
        return sanic.response.json({"status":400, "message":"Message is None."})
    async with aiohttp.ClientSession() as session:
        async with session.post(LINE_NOTIFY_URL, headers={"Authorization": f"Bearer {TOKEN}"}, data={"message": request.args.get("message")}) as response:
            return sanic.response.json(await response.json())

@app.route("/discord")
async def discord_notify(request: sanic.Request):
    _content = request.args.get("content")
    if _content is None:
        return sanic.response.json({"status":400, "message":"Content is None."})
    async with aiohttp.ClientSession() as session:
        await session.post(DISCORD_WEBHOOK_URL, data={"content": _content, "username": request.args.get("username", ""), "avatar_url": request.args.get("avatar_url", "")})
        return sanic.response.json({"status": 200, "content": _content})

if __name__ == "__main__":
    app.run(host=SETTING["host"], port=SETTING["port"])
