import pandas as pd
import altair as alt

from config import color_scale_scheme, axis_label_font_size, axis_title_font_size, axis_title_font_size2

df = pd.read_csv('data/response_data1.csv')

alt.Chart(df).mark_bar(size = 50).encode(
        x = 'start_percent2:Q',
        x2 = 'end_percent2:Q',
        fill = alt.Fill('response:N', scale = alt.Scale(scheme = color_scale_scheme))
).properties(
        height = 250,
        width = 400
).facet(
    row = 'field_name:N'
).configure_axis(
        labelFontSize = axis_label_font_size,
        titleFontSize = axis_title_font_size2
).configure_header(
        labelFontSize = axis_label_font_size,
        titleFontSize = axis_title_font_size
).save('div_bar6.json')

