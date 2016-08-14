from flask import Flask, jsonify, request
import unirest
import json
from ImgFeatureExtractor import ImgFeatureExtractor

app = Flask(__name__)

# slaves list here
Slaves = [
    'http://192.168.100.2:9101/compute',
    'http://192.168.100.3:9102/compute'
]

@app.route("/")
def status():
    res = {
        'status': '^_^',
        'msg': 'mrmaster'
    }
    return jsonify(res)

@app.route("/mcompute", methods=['PUT'])
def mcompute():
    res = {
        'status': '^_^',
        'msg': 'mrmaster',
        'data': []
    }

    file = request.files['file']
    file.save('/tmp/' + file.filename)
    ife = ImgFeatureExtractor('/tmp/' + file.filename)
    kp, data = ife.SURF()

    # data = FeatureMat[1][2]
    data = json.dumps(data.tolist())
    header = {"Content-Type": "application/json"}
    for slave in Slaves:
        response = unirest.put(url=slave, headers=header, params=data)
        res['data'].extend(response.body['data'])

    res['data'].sort(key=lambda x: x[1])
    return jsonify(res)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9100)
