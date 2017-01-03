from sanic import Sanic
from sanic.response import json
from redis import Redis

app = Sanic(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
async def test(request):
    count = redis.incr('hits')
    return json({"hello": f"I have been seen {count} timezzz."})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
