from flask import Flask, jsonify, request
import unirest
import json
from ImgFeatureExtractor import ImgFeatureExtractor

import pyocr
import pyocr.builders
import pytesseract
from PIL import Image

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

@app.route("/ocr")
def ocr():
    tools = pyocr.get_available_tools()
    tool = tools[0]
    print("Will use tool '%s'" % (tool.get_name()))

    langs = tool.get_available_languages()
    lang = langs[1]

    # ife = ImgFeatureExtractor('/tmp/9781111479022-1452074892070_spine.jpg')
    txt = tool.image_to_string(
        Image.open('/tmp/9781111479022-1452074892070_spine.jpg'),
        lang=lang,
        builder=pyocr.builders.TextBuilder()
    )
    print txt

    return 'ok'

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
