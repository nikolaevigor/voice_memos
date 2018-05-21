from sanic import Sanic
from sanic.response import json

app = Sanic()


@app.route('/')
async def ping(request):
    return json('pong')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
