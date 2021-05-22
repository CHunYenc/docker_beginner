from flask import Flask, render_template
from redis import Redis
import os
import socket

app = Flask(__name__)
redis = Redis(host="redis", port=6379)


@app.route("/")
def index():
    redis.incr("hits")
    return f'Hello Container World! I have been {redis.get("hits")} times and my hostname is {socket.gethostname()}'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
