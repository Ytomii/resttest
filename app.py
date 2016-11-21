#!/usr/bin/python
from flask import Flask, make_response, render_template, request
from array import array
import random, json

app = Flask(__name__)

def random_gen(low, high, count):
	randoms = []
	for i in range (count):   
		randoms.append(random.randrange(low,high,1))    
	#print(randoms)	
	return randoms


@app.route('/')
def test():
	a = request.args.get('a', type=int)
	b = request.args.get('b', type=int)
	if a > b:
		a, b = b, a
	mylist = random_gen(a, b+1, 10)

	#return mylist
	
	json_numbers = json.dumps(mylist)
	json.loads(json_numbers)
	return json_numbers
	#return render_template('index.html', mylist=mylist, json_numbers=json_numbers)

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)