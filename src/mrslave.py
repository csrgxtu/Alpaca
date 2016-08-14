from flask import Flask, jsonify
import pickle
app = Flask(__name__)

@app.route("/")
def status():
    res = {
        'status': '^_^',
        'msg': 'mrslave'
    }
    return jsonify(res)

@app.route("/compute")
def compute():
    res = {
        'data': []
    }
    return jsonify(res)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9101)
