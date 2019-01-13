import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import numpy as np
import retrieveData as dp
import hackv2 as parseData

def getDropDownValues():
    return [{'label': 'Action', 'value': 'Action'},
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


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



yearBeginnning = 1970
years = list(range(yearBeginnning, yearBeginnning+50))
numMales= np.random.randint(low=0, high=20, size=50)
numFemales= np.random.randint(low=0, high=20, size=50)




app.layout = html.Div(children=[
    html.H1('Horizon North'),
    html.Div([
    html.P('Genre trends across time'),
    html.P('This conversion happens behind the scenes by Dash JavaScript front-end')
    ]),
    dcc.Graph(id='freq-graph'),
    dcc.Dropdown(
        id='genre-type',
        options=getDropDownValues(),
        value='action'
    )
])


@app.callback(
    dash.dependencies.Output('freq-graph', 'figure'),
    [dash.dependencies.Input('genre-type', 'value')])

def update_graph(genreType):

    count = dp.genList(genreType.title())
    return {
            'data': [go.Scatter(
                x = [i for i in range(1950,2018)],
                y = count,
                mode = 'lines+markers',
                name = 'Count'
            )

            ]
        }

if __name__ == '__main__':
    app.run_server(debug=True)
