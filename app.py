from flask import Flask
from flask import jsonify
import usacorona
app = Flask(__name__)
app = Flask(__name__)


@app.route('/total', methods=['GET'])
def tot():
    return jsonify(usacorona.d)

@app.route('/')
def index():
    return jsonify(usacorona.d)
if __name__=="__main__":
    app.run(debug=True,host="127.0.0.1",port=4444)