from flask import Flask
import json

template = {"code": 0,  "msg": "", "data":{}}

app = Flask(__name__)

@app.route('/ping')
def ping():
    re = template
    re["data"] = {"msg": "pong"}
    return json.dumps(re)

if __name__ == '__main__':
    app.run()