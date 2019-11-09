import pandas as pd
from helper import setcols

df = pd.read_csv('data/scale_responses.csv')

c1 = df.groupby(['field_name', 'response'])['satisfaction_v2'].count()
f1 = c1.groupby(level=0).apply(lambda x: x / float(x.sum()))

c1 = pd.concat([c1, f1], axis = 1).pipe(setcols, cols = ['count', 'freq'])

idx = pd.IndexSlice

res = c1.loc[idx[['Baggage handling', 'Seat comfort'],:,:],:]
res = res.reset_index()

res['end_percent'] = res.groupby('field_name')['freq'].cumsum()
res['start_percent'] = res.groupby('field_name')['end_percent'].shift(1).fillna(0)
res['negative'] = res['response'].apply(lambda x: True if x < 3 else False)
starting_point = res[res.negative].groupby('field_name')['freq'].sum()
res = res.set_index(['field_name', 'response'])
res['end_percent2'] = res['end_percent'] - starting_point
res['start_percent2'] = res['start_percent'] - starting_point
res = res.reset_index()

res.to_csv('data/response_data1.csv')
        
