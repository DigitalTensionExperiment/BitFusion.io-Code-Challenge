from flask import Flask
from flask import jsonify

app = Flask(__name__)
app.config['SERVER_NAME'] = '127.0.0.1:8888'

@app.route('/hello', methods=['GET'])
def get_tasks():
    return jsonify({"result": "hello world"})

if __name__ == '__main__':
    print "Inside main..."
    app.run(debug=None)

