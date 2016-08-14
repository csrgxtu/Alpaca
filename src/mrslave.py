from flask import Flask, jsonify, request
import pickle
import numpy as np
import cv2
import json
import ast
app = Flask(__name__)

# load the pickle data into mem first, and make it global
FeatureMat = pickle.load(open('./FeatureMat.pkl', 'rb'))
BF = cv2.BFMatcher()

@app.route("/")
def status():
    res = {
        'status': '^_^',
        'msg': 'mrslave'
    }
    return jsonify(res)

@app.route("/compute", methods=['PUT'])
def compute():
    data = np.array(json.loads(request.data), dtype=np.float32)
    res = {
        'data': []
    }

    for row in FeatureMat:
        if row[2] is None:
            continue

        # data = FeatureMat[1][2] # temp
        matches = BF.knnMatch(data, row[2], k=2)
        matches = sorted(matches, key = lambda x:x[0].distance)
        Distance = []
        for m in matches:
            Distance.append(m[0].distance)
        res['data'].append([row[1], np.average(Distance)])

    res['data'].sort(key=lambda x: x[1])
    return jsonify(res)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9101)
