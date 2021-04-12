from flask import Flask, request, url_for, redirect, render_template, jsonify
import numpy as np
import pandas as pd
import pickle
from flask_bootstrap import Bootstrap
from predict import predict, predict2, predict3, predict4
app = Flask(__name__)




@app.route('/')
def home():
	return render_template("index.html")


@app.route('/daniel')
def daniel():
	return render_template('Daniel.html')

@app.route('/overview')
def overview():
	return render_template('project_overview.html')


@app.route('/data-dict')
def data_dict():
	return render_template('data-dict.html')

@app.route('/leisure-hosp', methods = ["POST", "GET"])
def leisure_hosp():
	if request.method=="POST":
		print(request.form)
		if request.form:
			try:
				steps=int(request.form.to_dict(flat=False)['steps'][0])
				print(steps)
				if steps<=12:
					prediction1 = predict(steps)
					prediction2 = predict2(steps)
					prediction3 = predict3(steps)
					prediction4 = predict4(steps)
					return render_template('leisure_hosp.html',steps = steps, prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
				else:
					steps = 12
					prediction1 = predict(steps)
					prediction2 = predict2(steps)
					prediction3 = predict3(steps)
					prediction4 = predict4(steps)
					return render_template('leisure_hosp.html',steps = steps, prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
			except:
				prediction1 = None
				prediction2 = None
				prediction3 = None
				prediction4 = None
				return render_template('leisure_hosp.html', prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
		else:
			prediction1 = None
			prediction2 = None
			prediction3 = None
			prediction4 = None
			return render_template('leisure_hosp.html', prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
	else:
		prediction1 = None
		prediction2 = None
		prediction3 = None
		prediction4 = None
		return render_template('leisure_hosp.html', prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)





@app.route('/retail', methods = ["POST", "GET"])
def retail():
	if request.method=="POST":


		print(request.form)
		if request.form:
			try:
				steps=int(request.form.to_dict(flat=False)['steps'][0])
				print(steps)
				if steps<=12:

					prediction1 = predict(steps)
					prediction2 = predict2(steps)
					prediction3 = predict3(steps)
					prediction4 = predict4(steps)
					return render_template('retail.html',steps = steps, prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
				else:
					steps = 12
					prediction1 = predict(steps)
					prediction2 = predict2(steps)
					prediction3 = predict3(steps)
					prediction4 = predict4(steps)
					return render_template('retail.html',steps = steps, prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
			except:
				prediction1 = None
				prediction2 = None
				prediction3 = None
				prediction4 = None
				return render_template('retail.html', prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)


		else:
			prediction1 = None
			prediction2 = None
			prediction3 = None
			prediction4 = None
			return render_template('retail.html', prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
	else:
		prediction1 = None
		prediction2 = None
		prediction3 = None
		prediction4 = None
		return render_template('retail.html', prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)



@app.route('/mining', methods = ["POST", "GET"])
def mining():
	if request.method=="POST":


		print(request.form)
		if request.form:
			try:
				steps=int(request.form.to_dict(flat=False)['steps'][0])
				print(steps)
				if steps<=12:

					prediction1 = predict(steps)
					prediction2 = predict2(steps)
					prediction3 = predict3(steps)
					prediction4 = predict4(steps)
					return render_template('mining.html',steps = steps, prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
				else:
					steps = 12
					prediction1 = predict(steps)
					prediction2 = predict2(steps)
					prediction3 = predict3(steps)
					prediction4 = predict4(steps)
					return render_template('mining.html',steps = steps, prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
			except:
				prediction1 = None
				prediction2 = None
				prediction3 = None
				prediction4 = None
				return render_template('mining.html', prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)


		else:
			prediction1 = None
			prediction2 = None
			prediction3 = None
			prediction4 = None
			return render_template('mining.html', prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
	else:
		prediction1 = None
		prediction2 = None
		prediction3 = None
		prediction4 = None
		return render_template('mining.html', prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)


@app.route('/construct', methods = ["POST", "GET"])
def construct():
	if request.method=="POST":


		print(request.form)
		if request.form:
			try:
				steps=int(request.form.to_dict(flat=False)['steps'][0])
				print(steps)
				if steps<=12:

					prediction1 = predict(steps)
					prediction2 = predict2(steps)
					prediction3 = predict3(steps)
					prediction4 = predict4(steps)
					return render_template('construction.html',steps = steps, prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
				else:
					steps = 12
					prediction1 = predict(steps)
					prediction2 = predict2(steps)
					prediction3 = predict3(steps)
					prediction4 = predict4(steps)
					return render_template('construction.html',steps = steps, prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
			except:
				prediction1 = None
				prediction2 = None
				prediction3 = None
				prediction4 = None
				return render_template('construction.html', prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)


		else:
			prediction1 = None
			prediction2 = None
			prediction3 = None
			prediction4 = None
			return render_template('construction.html', prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
	else:
		prediction1 = None
		prediction2 = None
		prediction3 = None
		prediction4 = None
		return render_template('construction.html', prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)


@app.route('/edu-health', methods = ["POST", "GET"])
def edu_healtht():
	if request.method=="POST":


		print(request.form)
		if request.form:
			try:
				steps=int(request.form.to_dict(flat=False)['steps'][0])
				print(steps)
				if steps<=12:

					prediction1 = predict(steps)
					prediction2 = predict2(steps)
					prediction3 = predict3(steps)
					prediction4 = predict4(steps)
					return render_template('edu.html',steps = steps, prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
				else:
					steps = 12
					prediction1 = predict(steps)
					prediction2 = predict2(steps)
					prediction3 = predict3(steps)
					prediction4 = predict4(steps)
					return render_template('edu.html',steps = steps, prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
			except:
				prediction1 = None
				prediction2 = None
				prediction3 = None
				prediction4 = None
				return render_template('edu.html', prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)


		else:
			prediction1 = None
			prediction2 = None
			prediction3 = None
			prediction4 = None
			return render_template('edu.html', prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
	else:
		prediction1 = None
		prediction2 = None
		prediction3 = None
		prediction4 = None
		return render_template('edu.html', prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)


@app.route('/manu', methods = ["POST", "GET"])
def manu():
	if request.method=="POST":


		print(request.form)
		if request.form:
			try:
				steps=int(request.form.to_dict(flat=False)['steps'][0])
				print(steps)
				if steps<=12:

					prediction1 = predict(steps)
					prediction2 = predict2(steps)
					prediction3 = predict3(steps)
					prediction4 = predict4(steps)
					return render_template('manu.html',steps = steps, prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
				else:
					steps = 12
					prediction1 = predict(steps)
					prediction2 = predict2(steps)
					prediction3 = predict3(steps)
					prediction4 = predict4(steps)
					return render_template('manu.html',steps = steps, prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
			except:
				prediction1 = None
				prediction2 = None
				prediction3 = None
				prediction4 = None
				return render_template('manu.html', prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)


		else:
			prediction1 = None
			prediction2 = None
			prediction3 = None
			prediction4 = None
			return render_template('manu.html', prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
	else:
		prediction1 = None
		prediction2 = None
		prediction3 = None
		prediction4 = None
		return render_template('manu.html', prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)

@app.route('/pro', methods = ["POST", "GET"])
def pro():
	if request.method=="POST":


		print(request.form)
		if request.form:
			try:
				steps=int(request.form.to_dict(flat=False)['steps'][0])
				print(steps)
				if steps<=12:

					prediction1 = predict(steps)
					prediction2 = predict2(steps)
					prediction3 = predict3(steps)
					prediction4 = predict4(steps)
					return render_template('profess.html',steps = steps, prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
				else:
					steps = 12
					prediction1 = predict(steps)
					prediction2 = predict2(steps)
					prediction3 = predict3(steps)
					prediction4 = predict4(steps)
					return render_template('profess.html',steps = steps, prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
			except:
				prediction1 = None
				prediction2 = None
				prediction3 = None
				prediction4 = None
				return render_template('profess.html', prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)


		else:
			prediction1 = None
			prediction2 = None
			prediction3 = None
			prediction4 = None
			return render_template('profess.html', prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
	else:
		prediction1 = None
		prediction2 = None
		prediction3 = None
		prediction4 = None
		return render_template('profess.html', prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)

@app.route('/govt', methods = ["POST", "GET"])
def govt():
	if request.method=="POST":


		print(request.form)
		if request.form:
			try:
				steps=int(request.form.to_dict(flat=False)['steps'][0])
				print(steps)
				if steps<=12:

					prediction1 = predict(steps)
					prediction2 = predict2(steps)
					prediction3 = predict3(steps)
					prediction4 = predict4(steps)
					return render_template('govt.html',steps = steps, prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
				else:
					steps = 12
					prediction1 = predict(steps)
					prediction2 = predict2(steps)
					prediction3 = predict3(steps)
					prediction4 = predict4(steps)
					return render_template('govt.html',steps = steps, prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
			except:
				prediction1 = None
				prediction2 = None
				prediction3 = None
				prediction4 = None
				return render_template('govt.html', prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)


		else:
			prediction1 = None
			prediction2 = None
			prediction3 = None
			prediction4 = None
			return render_template('govt.html', prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)
	else:
		prediction1 = None
		prediction2 = None
		prediction3 = None
		prediction4 = None
		return render_template('govt.html', prediction1=prediction1, prediction2=prediction2, prediction3=prediction3, prediction4=prediction4)







@app.route('/shweta')
def shweta():
	return render_template('shweta.html')

@app.route('/tony')
def tony():
	return render_template('tony.html')

@app.route('/isaiah')
def isaiah():
	return render_template('isaiah.html')

if __name__=="__main__":
	app.run(debug=False)
	app.run()
