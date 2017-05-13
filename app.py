from flask import Flask, jsonify, request
from flask.ext.pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = "trialdb2729"
app.config['MONGO_URI'] = "mongodb://sujaybr9:sujaybr9@ds159517.mlab.com:59517/trialdb2729"

mongo = PyMongo(app)

@app.route("/")
def home():
	return jsonify({'message': "it works"})

@app.route("/animals/")
def getanimals():
	data = mongo.db.animals
	out = []
	for i in data.find():
		#oid.append(i['_id'])
		out.append({"name":i['name']})		
	return jsonify({"result":out})

@app.route("/animals/<name>")
def getoneanimal(name):
	data = mongo.db.animals
	#out = []
	idofdata = data.find_one({"name":name})
	#realname = data.find_one({"_id":idofdata})
	if idofdata:
		out = {"name":idofdata['name']}
	else:
		out = "no output"
	return jsonify({"result":out})

@app.route("/animals",methods = ['POST'])
def putoneanimal():
	data = mongo.db.animals

	nameofanimal = request.json['name']
	idofanimal = data.insert({"name":nameofanimal})

	out = {"name":nameofanimal}
	return jsonify({"result":out})


if __name__ == "__main__":
	app.run(debug = True)