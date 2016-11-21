#!/usr/bin/python
from flask import Flask, make_response, request, jsonify
from array import array
from flask_httpauth import HTTPBasicAuth

import random, json
auth = HTTPBasicAuth()

app = Flask(__name__)

def random_gen(low, high, count):
	randoms = []
	for i in range (count):   
		randoms.append(random.randrange(low,high,1))    
	#print(randoms)	
	return randoms

@auth.get_password
def get_password(username):
    if username == 'yuji':
        return 'test123'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.route('/')
@auth.login_required
def test():
	a = request.args.get('a', type=int)
	b = request.args.get('b', type=int)
	if a > b:
		a, b = b, a
	mylist = random_gen(a, b+1, 10)

	
	json_numbers = json.dumps(mylist)
	#json.loads(json_numbers)
	return json_numbers

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)