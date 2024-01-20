import json
from flask import Flask, request, jsonify
from temp import temperature



# Vairabless
total_requests = 0

#App
app = Flask(__name__)
@app.route('/')
def index():
    counter()

    return json.dumps({'status': 200,
                       'owner': 'brandon'})

@app.route('/requests')
def requests():
    counter()
    global total_requests
    return json.dumps({'total': str(total_requests)})

@app.route('/name', methods=['GET'])
def name():
    counter()
    args = request.args
    name = args.get('name')

    return json.dumps({'Hello there': name})

#Temperature API
# name , toke, probe_id , temp
@app.route('/temp_upload')
def temp_upload():
    counter()
    args = request.args
    x = temperature.upload_temperature(args.get('name'), args.get('token'), args.get('probe_id'), args.get('temp'))
    return json.dumps({'status': x})

# name , toke, probe_id , amount of points
@app.route('/temp_collect')
def temp_collect():
    counter()
    args = request.args
    x = temperature.get_temperature(args.get('name'), args.get('token'), args.get('probe_id'), args.get('amount'))
    return json.dumps(x)


#Counter for the data
def counter():
    global total_requests
    total_requests += 1

app.run(host='0.0.0.0', port=5000)


