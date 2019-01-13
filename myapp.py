import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import numpy as np
import retrieveData as dp
import hackv2 as parseData

def getDropDownValues():
    return [
{'label': 'All Movies', 'value' : 'All'},
{'label': 'Action', 'value': 'Action'},
{'label': 'Adventure', 'value': 'Adventure'},
{'label': 'Animation', 'value': 'Animation'},
{'label': 'Comedy', 'value': 'Comedy'},
{'label': 'Crime', 'value': 'Crime'},
{'label': 'Documentary', 'value': 'Documentary'},
{'label': 'Drama', 'value': 'Drama'},
{'label': 'Family', 'value': 'Family'},
{'label': 'Fantasy', 'value': 'Fantasy'},
{'label': 'Foreign', 'value': 'Foreign'},
{'label': 'History', 'value': 'History'},
{'label': 'Horror', 'value': 'Horror'},
{'label': 'Music', 'value': 'Music'},
{'label': 'Mystery', 'value': 'Mystery'},
{'label': 'Romance', 'value': 'Romance'},
{'label': 'Science Fiction' , 'value': 'Science Fiction' },
{'label': 'TV' , 'value': 'Tv' },
{'label': 'Thriller', 'value': 'Thriller'},
{'label': 'War', 'value': 'War'},
{'label': 'Western', 'value': 'Western'}]


external_stylesheets = ['assets/styles.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



app.layout = html.Div(children=[
        html.H1(children='Horizon North',
                    style = {
                'text-align': 'center', 'color': 'white'}),
            html.Div([
            html.H2(children='Movie genre trends across time (1950-2017)',
                   style = {'text-align': 'center', 'color': 'white'
                    }),
            ]),       
    dcc.Graph(id='freq-graph'),
    dcc.Dropdown(
        id='genre-type',
        options=getDropDownValues(),
        value=['all'],
        multi=True
    )
],
                      style ={'background-image': 'linear-gradient(to right, #909090 ,#181818)',
                               'font-family':'Optima, sans-serif'}                      )


@app.callback(
    dash.dependencies.Output('freq-graph', 'figure'),
    [dash.dependencies.Input('genre-type', 'value')])

def update_graph(genreType):
 
    traces = []
    years = [i for i in range(1950,2018)]
    for genre in genreType:
        if (genre.lower() == 'all'):
        
            trace = go.Scatter(
                    x = years[:len(years)-1],
                    y = dp.genTotal()[:-1],
                    mode = 'lines+markers',
                    name = genre
                )
        else:
            
            trace = go.Scatter(
                    x = years,
                    y = dp.genList(genre.title())[:-1],
                    mode = 'lines+markers',
                    name = genre
                )
        traces.append(trace)

    count = [i for i in range(1950,2018)]
    return {
            'data': traces,
            #'layout': {
             #   'paper_bgcolor':'#C0C0C0'
            #}            
        }

if __name__ == '__main__':
    app.run_server(debug=True)
