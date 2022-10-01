import sanic
import aiohttp
import os
import sys
import json

app = sanic.Sanic(__name__)

URL = "https://notify-api.line.me/api/notify"

SETTING = json.load(open("secret.json", "r"))
TOKEN = SETTING["token"]


@app.route("/")
async def main_root(request: sanic.Request):
    return sanic.response.json({"Service":"Available"})

@app.route("/notify")
async def line_notify(request: sanic.Request):
    if request.args.get("message") is None:
        return sanic.response.json({"status":400, "message":"Message is None."})
    async with aiohttp.ClientSession() as session:
        async with session.post(URL, headers={"Authorization": f"Bearer {TOKEN}"} , data={"message": request.args.get("message")}) as response:
            print(response.status)
            return sanic.response.json(await response.json())

if __name__ == "__main__":
    app.run(host=SETTING["host"], port=SETTING["port"])
