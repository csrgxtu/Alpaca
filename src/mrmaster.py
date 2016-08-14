from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def status():
    res = {
        'status': '^_^',
        'msg': 'mrmaster'
    }
    return jsonify(res)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9100)
