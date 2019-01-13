import pandas as pd
import numpy as np
import json

genreData = pd.read_csv('data/movies_metadata2.csv', usecols = ['genres'])
data = pd.read_csv('data/movies_metadata.csv', usecols = ['title','genres','vote_average','release_date','id'])

listgenre = []
for key, value in genreData.iteritems():
    for val in value:
        val = json.loads(val)
        if (len(val) > 0):
            genre = (val[0]['name'])
            listgenre.append(genre)
        else:
            listgenre.append('NaN')

df = pd.DataFrame(listgenre)
data['genres'] = df
data = data[data['genres'] != 'NaN']
data = data[data['genres'] != 'Odyssey Media']
data = data[data['genres'] != 'Aniplex']
data = data[data['genres'] != 'Carousel Productions']

# change object into datetime then sort by release date descending old -> new
data.dropna(how='any', inplace=True)
data['release_date'] =  data['release_date'].astype('datetime64[ns]')
data = data[(data['release_date'].dt.year >= 1950) & (data['release_date'].dt.year != 2018) & (data['release_date'].dt.year != 2020)]

data.sort_values(by=['release_date'], inplace=True, ascending=True)

# change vote average from object to int then sort values
data['vote_average'] = data['vote_average'].fillna(0).astype(np.int)
data.sort_values(by=['vote_average'], inplace=True, ascending=True)

data.to_csv('out.csv', encoding='utf-8', index=True)
