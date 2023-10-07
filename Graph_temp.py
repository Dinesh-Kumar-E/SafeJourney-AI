import dash
from dash.dependencies import Output, Input
from dash import dcc
from dash import html
import plotly

import plotly.graph_objs as go
from collections import deque


import Face_data

def ear_mar():
        x = Face_data.EAR_MAR()
        return x[0], x[1]

X = deque(maxlen=20)
X.append(0.5)

Y1 = deque(maxlen=20)
Y1.append(0.5)

Y2 = deque(maxlen=20)
Y2.append(0.5)


app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1*1000
        ),
    ]
)

@app.callback(Output('live-graph', 'figure'),[Input('graph-update', 'n_intervals')])
def update_graph_scatter(n):

    X.append(X[-1]+1)
    while True:
        try:
            res = ear_mar()
            Y1.append(res[0])
            Y2.append(res[1])
            break
        except Exception as exception:
            print(exception)
            continue

    data1 = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y1),
            name='Scatter',
            mode= 'lines+markers'
            )
    
    data2 = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y2),
            name='Scatter',
            mode= 'lines+markers'
            )

    return {'data': [data1,data2],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
                                                yaxis=dict(range=[min(Y2),max(Y2)]),)}


if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1', port=8080)