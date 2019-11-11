import pandas as pd
import altair as alt

from config import color_scale_scheme, axis_label_font_size, axis_title_font_size, axis_title_font_size2

df = pd.read_csv('data/response_data1.csv')

alt.Chart(df).mark_bar().encode(
        x = 'start_percent:Q',
        x2 = 'end_percent:Q',
        fill = alt.Fill('response:N', scale = alt.Scale(scheme = color_scale_scheme))
).properties(
        height = 250,
        width = 400
).facet(
    row = 'field_name:N'
).save('div_bar5.json')

