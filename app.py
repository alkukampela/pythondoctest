from sanic import Sanic
from sanic.response import json
from redis import Redis

app = Sanic(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
async def test(request):
    count = redis.incr('hits')
    return json({"hello": "I have been seen {} timezzz.".format(count)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
