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
import predictor
import numpy as np

def log(content):
    with open("logs\log.txt", "a") as file:
        file.write(content + "\n")

def ear_mar():
    x = Face_data.EAR_MAR()
    return x[0], x[1], x[2]

deque_size = 10

X = deque(maxlen=deque_size)
X.append(0.5)

Y1 = deque(maxlen=deque_size)
Y1.append(0.5)

Y2 = deque(maxlen=deque_size)
Y2.append(0.5)

update_frequency = 100

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Interval(
        id='graph-update',
        interval=update_frequency
    ),
    html.Div([
        html.Div([
            html.H1(children='Eye Aspect Ratio'),
            html.Div(children='''
                LIVE EAR 
            '''),
            dcc.Graph(
                id='graph1',
                figure={}
            ),  
        ], className='six columns'),
        
        html.Div([
            html.H1(children='Mouth Aspect Ratio'),
            html.Div(children='''
                LIVE MAR
            '''),
            dcc.Graph(
                id='graph2',
                figure={}
            ),  
        ], className='six columns'),
    ], className='row'),
    
    html.Div([
        html.Div([
            html.H2(children="DRIVER'S STATUS:"),
            html.P(id='dynamic-text'),  # Placeholder for dynamic text
        ], className='six columns'),
        
        html.Div([
            html.H1(children='Face Feature Points'),
            dcc.Graph(
                id='scatter-graph',
                figure={}
            ),  
        ], className='six columns'),
    ], className='row')
])

def update_graph_scatter(n):
    X.append(X[-1]+1)
    face = None
    while True:
        try:
            res = ear_mar()
            s, t = res[0], res[1]
            Y1.append(s)
            Y2.append(t)
            log(str(s) + " " + str(t))
            face = res[2]
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
    x_face = np.array(face[0])
    y_face = np.array(face[1])
    x_face = -1*x_face
    y_face = -1*y_face
    
    return [
        {'data': [data1], 'layout': go.Layout(xaxis=dict(range=[min(X), max(X)]),
                                              yaxis=dict(range=[0,1]))},
        {'data': [data2], 'layout': go.Layout(xaxis=dict(range=[min(X), max(X)]),
                                              yaxis=dict(range=[0,4]))},
        {'data': [go.Scatter(x=x_face, y=y_face, mode='markers')],
         'layout': go.Layout(xaxis=dict(range=[min(x_face), max(x_face)]),
                             yaxis=dict(range=[min(y_face), max(y_face)]))}
    ]

@app.callback([Output('graph1', 'figure'),Output('graph2', 'figure'), Output('scatter-graph', 'figure'), Output('dynamic-text', 'children')],
              Input('graph-update', 'n_intervals'))
def update_graph(n):
    figures = update_graph_scatter(n)
    status = predictor.classify(Y1, Y2, "default")
    dynamic_text = "NORMAL" if status == 0 else "DROWSY"
    return figures[0],figures[1],figures[2], dynamic_text

if __name__ == '__main__':
    app.run_server(debug=True)
