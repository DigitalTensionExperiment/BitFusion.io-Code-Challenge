from flask import Flask
from flask import jsonify

app = Flask(__name__)
app.config['SERVER_NAME'] = '0.0.0.0:8888'

@app.route('/hello', methods=['GET'])
def get_tasks():
    print "Inside flaskHello:get_tasks..."
    return jsonify({"result": "hello world"})

if __name__ == '__main__':
    print "Inside flaskHello:main..."
    app.run(debug=None)

