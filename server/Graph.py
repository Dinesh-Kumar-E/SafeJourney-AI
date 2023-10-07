import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from collections import deque
import pandas as pd
import plotly.graph_objs as go
import sys
sys.path.append("modules")
import Face_data

def log(content):
    with open("logs\log.txt", "a") as file:
        file.write(content + "\n")

def ear_mar():
    x = Face_data.EAR_MAR()
    return x[0], x[1]

X = deque(maxlen=20)
X.append(0.5)

Y1 = deque(maxlen=20)
Y1.append(0.5)

Y2 = deque(maxlen=20)
Y2.append(0.5)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Interval(
        id='graph-update',
        interval=1*1000
    ),
    html.Div([
        html.Div([
            html.H1(children='EAR'),

            html.Div(children='''
                Dash: LIVE EAR.
            '''),

            dcc.Graph(
                id='graph1',
                figure={} 
            ),  
        ], className='six columns'),
        html.Div([
            html.H1(children='MAR'),

            html.Div(children='''
                Dash: LIVE MAR.
            '''),

            dcc.Graph(
                id='graph2',
                figure={}
            ),  
        ], className='six columns'),
    ], className='row'),
])

def update_graph_scatter(n):
    X.append(X[-1]+1)
    while True:
        try:
            res = ear_mar()
            s, t = res[0], res[1]
            print(s, t)
            Y1.append(s)
            Y2.append(t)
            log(str(s) + " " + str(t))
            break
        except Exception as exception:
            print(exception)
            continue

    data1 = go.Scatter(
        x=list(X),
        y=list(Y1),
        name='EAR',
        mode='lines+markers'
    )
    
    data2 = go.Scatter(
        x=list(X),
        y=list(Y2),
        name='MAR',
        mode='lines+markers'
    )

    return [{'data': [data1], 'layout': go.Layout(xaxis=dict(range=[min(X), max(X)]),
                                                  yaxis=dict(range=[min(Y1), max(Y1)]))},
            {'data': [data2], 'layout': go.Layout(xaxis=dict(range=[min(X), max(X)]),
                                                  yaxis=dict(range=[min(Y2), max(Y2)]))}]

@app.callback(Output('graph1', 'figure'), Output('graph2', 'figure'), Input('graph-update', 'n_intervals'))
def update_graph(n):
    figures = update_graph_scatter(n)
    return figures[0], figures[1]

if __name__ == '__main__':
    app.run_server(debug=True)
