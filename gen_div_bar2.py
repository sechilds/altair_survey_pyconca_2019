import pandas as pd
import altair as alt

df = pd.read_csv('data/response_data1.csv')

alt.Chart(df).mark_bar().encode(
        x = 'freq:Q',
        y = 'response:N',
        fill = alt.Fill('response:N', scale = alt.Scale(scheme = 'dark2'))
).facet(
    row = 'field_name:N'
).save('div_bar2.json')

