import pandas as pd
from helper import setcols

df = pd.read_excel('data/customer-satisfaction/satisfaction.xlsx')

df = df.set_index('id')

long_data = (df.stack()
          .reset_index()
          .pipe(setcols,
                cols = ['id', 'field_name', 'response'])
          .set_index('id')
       )

long_data = pd.merge(long_data, df, how = 'inner', left_index = True, right_index = True)

scales = ['Seat comfort',
       'Departure/Arrival time convenient', 'Food and drink', 'Gate location',
       'Inflight wifi service', 'Inflight entertainment', 'Online support',
       'Ease of Online booking', 'On-board service', 'Leg room service',
       'Baggage handling', 'Checkin service', 'Cleanliness', 'Online boarding']

scale_responses = long_data[long_data.field_name.apply(lambda x : x in scales)]

scale_responses.to_csv('data/scale_responses.csv')
