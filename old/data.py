from pandas.core.frame import DataFrame
import pandas_datareader as pdr
import plotly.graph_objects as go
import datetime 

import numpy as np
from sklearn.linear_model import LinearRegression

def get_data(company : str, date_start : datetime, date_end : datetime = datetime.datetime.today()) -> DataFrame:
    return pdr.get_data_yahoo(symbols=company, start=date_start, end=date_end)

def get_OHLC(company : str, date_start : datetime, date_end : datetime = datetime.datetime.today()):
    df = get_data(company, date_start, date_end)
    return go.Figure(data=go.Ohlc(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close']))

def get_graps_avr_hl(company : str, date_start : datetime, date_end : datetime = datetime.datetime.today()):
    df = get_data(company, date_start, date_end)
    avr = (df['High'] + df['Low']) / 2
    return get_graph(avr)

def get_graps_avr_oc(company : str, date_start : datetime, date_end : datetime = datetime.datetime.today()):
    df = get_data(company, date_start, date_end)
    avr = (df['Open'] + df['Close']) / 2
    return get_graph(avr)

def get_graps_diff_hl(company : str, date_start : datetime, date_end : datetime = datetime.datetime.today()):
    df = get_data(company, date_start, date_end)
    diff = abs(df['High'] - df['Low'])
    return get_graph(diff)

def get_graps_diff_oc(company : str, date_start : datetime, date_end : datetime = datetime.datetime.today()):
    df = get_data(company, date_start, date_end)
    diff = abs(df['Open'] - df['Close'])
    return get_graph(diff)

def parse_data(data : DataFrame):
    date, values = data.index.values, data.values

    x_train_date, x_train_value = date[:len(date) - 1], values[:len(date) - 1]
    y_train_date, y_train_value = date[1:], values[1:]

    return {'input_data': 
                [{'x':x_train_date, 'y': x_train_value},
                {'x':y_train_date, 'y': y_train_value}],
            'train_data': 
                {'x': x_train_value, 'y': y_train_value}}


def linear_reg(data):
    x = np.array(data['x']).reshape((-1, 1))
    y = np.array(data['y'])
    model = LinearRegression().fit(x, y)
   
    r_sq = model.score(x, y)
    info_reg = {
        'coeff_det': r_sq,
        'intercept' : model.intercept_,
        'slope' :  model.coef_ }

    y_pred = model.predict(x)
    result = [{'x': data['x'], 'y': data['y']}, {'x': data['x'], 'y': y_pred}]
    return result, info_reg


def get_figure(data):
    fig = go.Figure()
    [fig.add_trace(go.Scatter(x = item['x'], y = item['y'], mode="markers")) for item in data]
    return fig

def get_graph(value):
    data = parse_data(value)
    data_lear, _ = linear_reg(data['train_data'])
    fig = get_figure(data_lear)

    return fig


