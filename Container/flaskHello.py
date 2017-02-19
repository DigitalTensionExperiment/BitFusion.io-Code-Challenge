from flask import Flask
from flask import jsonify

app = Flask(__name__)
# app.config['SERVER_NAME'] = '0.0.0.0:8888'
#app.config['SERVER_NAME'] = '127.0.0.1:8888'


@app.route('/hello', methods=['GET'])
def get_tasks():
    print "Inside flaskHello:get_tasks..."
    return jsonify({"result": "hello world"})

