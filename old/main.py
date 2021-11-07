import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

import datetime as date

from data import *
from company import COMPANY

now = date.datetime.now()

app = dash.Dash()
app.layout = html.Div([
    html.H1(children='Биржевые индексы'),
    dcc.DatePickerRange(id='date_range_stock', start_date=now, end_date=now, display_format='DD-MM-YY'),
    dcc.Dropdown(id='dropdown_stock', options=COMPANY, value=None),
    html.Button(id='button_stock', children='Submit', ),
    html.Div(id='figure_stock'),

    html.H1(children='Прогнозирование по среднему High-Low'),
    dcc.DatePickerRange(id='date_range_avr_hl', start_date=now, end_date=now, display_format='DD-MM-YY'),
    dcc.Dropdown(id='dropdown_avr_hl', options=COMPANY, value=None),
    html.Button(id='button_avr_hl', children='Submit'),
    html.Div(id='figure_avr_hl'),

    html.H1(children='Прогнозирование по среднему Open-Close'),
    dcc.DatePickerRange(id='date_range_avr_oc', start_date=now, end_date=now, display_format='DD-MM-YY'),
    dcc.Dropdown(id='dropdown_avr_oc', options=COMPANY, value=None),
    html.Button(id='button_avr_oc', children='Submit'),
    html.Div(id='figure_avr_oc', children=[]),

    html.H1(children='Прогнозирование по разнице High-Low'),
    dcc.DatePickerRange(id='date_range_diff_hl', start_date=now, end_date=now, display_format='DD-MM-YY'),
    dcc.Dropdown(id='dropdown_diff_hl', options=COMPANY, value=None),
    html.Button(id='button_diff_hl', children='Submit'),
    html.Div(id='figure_diff_hl', children=[]),

    html.H1(children='Прогнозирование по разнице Open-Close'),
    dcc.DatePickerRange(id='date_range_diff_oc', start_date=now, end_date=now, display_format='DD-MM-YY'),
    dcc.Dropdown(id='dropdown_diff_oc', options=COMPANY, value=None),
    html.Button(id='button_diff_oc', children='Submit'),
    html.Div(id='figure_diff_oc', children=[]),
])

@app.callback(
    Output('figure_stock', 'children'),
    Input('button_stock', 'n_clicks'),
    State('dropdown_stock', 'value'),
    State('date_range_stock', 'start_date'),
    State('date_range_stock', 'end_date'))
def update_output(_, value : str, start_date : date.datetime, end_date: date.datetime):
    if value == None: return
    if start_date == end_date: return
    return dcc.Graph(figure=get_OHLC(value, start_date, end_date))

@app.callback(
    Output('figure_avr_hl', 'children'),
    Input('button_avr_hl', 'n_clicks'),
    State('dropdown_avr_hl', 'value'),
    State('date_range_avr_hl', 'start_date'),
    State('date_range_avr_hl', 'end_date'))
def update_output(_, value : str, start_date : date.datetime, end_date: date.datetime):
    if value == None: return
    if start_date == end_date: return
    return dcc.Graph(figure=get_graps_avr_hl(value, start_date, end_date))

@app.callback(
    Output('figure_avr_oc', 'children'),
    Input('button_avr_oc', 'n_clicks'),
    State('dropdown_avr_oc', 'value'),
    State('date_range_avr_oc', 'start_date'),
    State('date_range_avr_oc', 'end_date'))
def update_output(_, value : str, start_date : date.datetime, end_date: date.datetime):
    if value == None: return
    if start_date == end_date: return
    return dcc.Graph(figure=get_graps_avr_oc(value, start_date, end_date))

@app.callback(
    Output('figure_diff_hl', 'children'),
    Input('button_diff_hl', 'n_clicks'),
    State('dropdown_diff_hl', 'value'),
    State('date_range_diff_hl', 'start_date'),
    State('date_range_diff_hl', 'end_date'))
def update_output(_, value : str, start_date : date.datetime, end_date: date.datetime):
    if value == None: return
    if start_date == end_date: return
    return dcc.Graph(figure=get_graps_diff_hl(value, start_date, end_date))

@app.callback(
    Output('figure_diff_oc', 'children'),
    Input('button_diff_oc', 'n_clicks'),
    State('dropdown_diff_oc', 'value'),
    State('date_range_diff_oc', 'start_date'),
    State('date_range_diff_oc', 'end_date'))
def update_output(_, value : str, start_date : date.datetime, end_date: date.datetime):
    if value == None: return
    if start_date == end_date: return
    return dcc.Graph(figure=get_graps_diff_oc(value, start_date, end_date))

if __name__ == '__main__':
    app.run_server(debug=True)

