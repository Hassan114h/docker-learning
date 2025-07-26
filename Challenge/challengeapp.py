# app.py

from flask import Flask
import redis

app = Flask(__name__)
redis_server = redis.Redis(host='redishost', port=6379)

@app.route('/')
def hello_world():
    return 'Hello, World'

@app.route('/count')
def count():
    count = redis_server.incr('visitor_count')
    return f'This is visit count: {count}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)