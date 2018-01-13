"""Cloud Foundry test"""
from flask import Flask, render_template, request
import os

app = Flask(__name__)

if os.getenv("VCAP_APP_PORT"):
	port = int(os.getenv("VCAP_APP_PORT"))
else:
	port = 8080

@app.route('/', methods=['GET'])
def display_template():
	if "lower" in request.args:
		return request.args["lower"].lower()	
	elif "upper" in request.args:
		return request.args["upper"].upper()
	else: 			
		return render_template('index.html')	

from GunClock import GunClock

@app.route('/gunclock', methods=['GET'])
def display_gunclock():
	if "size" in request.args:
		gunclockSize=int(request.args["size"])
	else:
		gunclockSize=18

	if "color" in request.args:
		gunclockColor=request.args["color"]
	else:
		gunclockColor="ffffcc"

	gunclockStr = GunClock(gunclockSize).toString()
#	return ("<pre>" + gunclockStr + "</pre>")
	return render_template('gunclock.html', gunclockStr=gunclockStr, gunclockColor=gunclockColor, gunclockSize=str(gunclockSize))


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=port, debug=True)
