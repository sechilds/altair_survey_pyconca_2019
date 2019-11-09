import pandas as pd
from helper import setcols

df = pd.read_csv('data/scale_responses.csv')

c1 = df.groupby(['field_name', 'response'])['satisfaction_v2'].count()
f1 = c1.groupby(level=0).apply(lambda x: x / float(x.sum()))

c1 = pd.concat([c1, f1], axis = 1).pipe(setcols, cols = ['count', 'freq'])

idx = pd.IndexSlice

res = c1.loc[idx[['Baggage Handling', 'Seat Comfort'],:,:],:]
res = res.reset_index()

res.to_csv('data/response_data1.csv')
        
