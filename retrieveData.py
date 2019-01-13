import pandas as pd

data = pd.read_csv('out.csv', usecols = ['title','genres','vote_average','release_date','id'])
data['release_date'] =  data['release_date'].astype('datetime64[ns]')

def genList(genre):
    amountperGenre = []
    for i in range(1950,2018):
        temp = data.loc[(data['release_date'].dt.year == i) & (data['genres'] == genre)] #'Action'
        amountperGenre.append(temp.shape[0])
    #print(amountperGenre)
    return amountperGenre
# generates total movies for that year
def genTotal():
    total = []
    for i in range(1950,2018):
        temp = data.loc[(data['release_date'].dt.year == i)]
        total.append(temp.shape[0])
    return total

if __name__ == '__main__':

    genList(genre)
