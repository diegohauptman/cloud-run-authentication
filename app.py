from flask import Flask, request, Response
import logging

app = Flask(__name__)


@app.route('/')
def hello_world():
    result = ''
    for key in request.headers:
        result += str(key) + '\n'
    logging.warn(result)
    return Response(result, mimetype='text/plain')


if __name__ == "__main__":
    app.run(debug=True)
