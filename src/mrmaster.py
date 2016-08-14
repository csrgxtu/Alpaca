from flask import Flask, jsonify
import pickle
import unirest
import json
app = Flask(__name__)

# only for test
FeatureMat = pickle.load(open('./FeatureMat.pkl', 'rb'))

@app.route("/")
def status():
    res = {
        'status': '^_^',
        'msg': 'mrmaster'
    }
    return jsonify(res)

@app.route("/mcompute")
def mcompute():
    res = {
        'status': '^_^',
        'msg': 'mrmaster',
        'data': []
    }

    url = 'http://localhost:9101/compute'
    data = FeatureMat[1][2]
    data = json.dumps(data.tolist())
    header = {"Content-Type": "application/json"}
    response = unirest.put(url=url, headers=header, params=data)
    res['data'].extend(response.body['data'])

    return jsonify(res)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9100)
