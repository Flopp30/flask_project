'''
Основной файл с контролерами
'''
from time import time

from flask import Flask, Response, request, g

app = Flask(__name__)


@app.route('/<string:city>', methods=["GET", "POST"])
def index(city: str):
    name = request.args.get('name', None)
    if request.method == 'GET':
        return Response(f'Hello {city}!', 200)
    else:
        return Response(f'Hello {name}!', 200)


@app.before_request
def process_before_request():
    '''
    Sets start time to 'g' object
    '''
    g.start_time = time()


@app.after_request
def process_after_request(response):
    '''
    Adds process time in headers
    '''
    if hasattr(g, 'start_time'):
        response.headers["process-time"] = time() - g.start_time


@app.errorhandler(404)
def handler_404(error):
    app.logger.error(error)
    return '404'
