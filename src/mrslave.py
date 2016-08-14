from flask import Flask, jsonify
import pickle
app = Flask(__name__)

# load the pickle data into mem first, and make it global
FeatureMat = pickle.load(open('./FeatureMat.pkl', 'rb'))

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
    res['data'] = [x[0] for x in FeatureMat]

    return jsonify(res)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9101)
