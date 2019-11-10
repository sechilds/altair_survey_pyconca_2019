import pandas as pd
import altair as alt

from config import color_scale_scheme, axis_label_font, axis_title_font


df = pd.read_csv('data/response_data1.csv')

alt.Chart(df).mark_bar().encode(
        x = 'count:Q',
        y = 'response:N',
        fill = alt.Fill('response:N', scale = alt.Scale(scheme = color_scale_scheme))
).facet(
    row = 'field_name:N'
).configure_axis(
        labelFontSize = axis_label_font
        titleFontSize = axis_title_font
).save('div_bar1.json')

