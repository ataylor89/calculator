from flask import request, render_template, jsonify
from calculator import app, eval

@app.route('/evaluate', methods=['POST'])
def evaluate():
    expression = request.form['expression']
    result = eval.eval(expression)
    resp = {}
    resp['result'] = result
    return jsonify(resp)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
