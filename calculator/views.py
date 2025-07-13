from flask import request, render_template, jsonify
from calculator import app, eval
from pprint import pprint

@app.route('/evaluate', methods=['POST'])
def evaluate():
    print("Calling evaluate function...")
    
    pprint(request.form)

    pprint(request.form['expression'])

    expression = request.form['expression']
    result = eval.eval(expression)
    resp = {}
    resp['result'] = result

    print('Result = %s', result)

    return jsonify(resp)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
