import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

from statsmodels.tsa.api import VAR, VARMAX
import pickle

def invert_transformation(pred):
    forecast = pred.copy()
    columns = targets.columns

    for col in columns:
        forecast[col+'_preds'] = forecast[col +'_preds'].cumsum() + targets[col].iloc[-1]

    return forecast


def invert_transformation(pred, targets):
    forecast = pred.copy()
    columns = targets.columns

    for col in columns:
        forecast[col+'_preds'] = forecast[col +'_preds'].cumsum() + targets[col].iloc[-1]

    return forecast


def predict(var):
	targets = ['target_retail', 'target_mining_logging', 'target_construction',
       'target_edu_health', 'target_manufacturing', 'target_prof_business',
       'target_gov', 'target_leisure_hospitality']
	initial={'target_retail':15247.2,'target_mining_logging':589,'target_construction':7340,'target_edu_health':23267,'target_manufacturing':12238, 'target_prof_business': 20698,'target_gov':21446,'target_leisure_hospitality':13464}
	model = pickle.load(open('modelCOVNUM.sav', 'rb'))
	results = model.fit(maxlags=9, ic='aic')
	preds = results.forecast(y=results.endog, steps=var, exog_future=results.exog[-var:])
	preds= pd.DataFrame(preds, columns = targets)
	preds = preds.to_dict(orient='list')
	forecast = preds.copy()
	for i in targets:
		print(i)
		forecast[i] = round(sum(forecast[i]) + initial[i], 2)

	return forecast

def predict2(var):

	targets = ['target_retail', 'target_mining_logging', 'target_construction',
	'target_edu_health', 'target_manufacturing', 'target_prof_business',
	'target_gov', 'target_leisure_hospitality']
	initial={'target_retail':0.002703,'target_mining_logging':-0.0134,'target_construction':-0.008242,'target_edu_health':0.001895,'target_manufacturing':0.001719, 'target_prof_business': 0.003053,'target_gov':-0.003994,'target_leisure_hospitality':0.027081}

	model = pickle.load(open('model_PCTCOV.sav', 'rb'))
	results = model.fit(maxlags=13, ic='aic')
	preds = results.forecast(y=results.endog, steps=var, exog_future=results.exog[-var:])
	preds= pd.DataFrame(preds, columns = targets)
	preds = preds.to_dict(orient='list')
	forecast = preds.copy()
	for i in targets:
		print(i)
		forecast[i] = round(sum(forecast[i]) + initial[i], 4)

	return forecast

def predict3(var):

	targets = ['target_retail', 'target_mining_logging', 'target_construction',
	'target_edu_health', 'target_manufacturing', 'target_prof_business',
	'target_gov', 'target_leisure_hospitality']
	initial={'target_retail':15609.8,'target_mining_logging':690,'target_construction':7648,'target_edu_health':24565,'target_manufacturing':12799, 'target_prof_business': 21469,'target_gov': 22835,'target_leisure_hospitality': 16915}

	model = pickle.load(open('modelNOCOVNUM.sav', 'rb'))
	results = model.fit(maxlags=5, ic='aic')
	preds = results.forecast(y=results.endog, steps=var, exog_future=results.exog[-var:])
	preds= pd.DataFrame(preds, columns = targets)
	preds = preds.to_dict(orient='list')
	forecast = preds.copy()
	for i in targets:
		print(i)
		forecast[i] = round(sum(forecast[i]) + initial[i], 4)

	return forecast


def predict4(var):

	targets = ['target_retail', 'target_mining_logging', 'target_construction',
	'target_edu_health', 'target_manufacturing', 'target_prof_business',
	'target_gov', 'target_leisure_hospitality']
	initial={'target_retail':0.000295,'target_mining_logging':0.001451,'target_construction':0.004334,'target_edu_health':0.002121,'target_manufacturing':0.000547, 'target_prof_business': 0.001493,'target_gov':0.002019,'target_leisure_hospitality':0.003381}

	model = pickle.load(open('modelNOCOVPCT.sav', 'rb'))
	results = model.fit(maxlags=13, ic='aic')
	preds = results.forecast(y=results.endog, steps=var, exog_future=results.exog[-var:])
	preds= pd.DataFrame(preds, columns = targets)
	preds = preds.to_dict(orient='list')
	forecast = preds.copy()
	for i in targets:
		print(i)
		forecast[i] = round(sum(forecast[i]) + initial[i], 4)

	return forecast











if __name__== '__main__':
	print('testing functionality')
	steps=9

	pred = predict(steps)
	print(pred[0])
