from sanic import Sanic
from sanic.response import json,text

app = Sanic()

@app.route("/alive")
async def running(req):
    return text("RUNNING")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
  