import pandas as pd
import altair as alt

from config import dark2_colours, axis_label_font_size, axis_title_font_size

datasaurus = pd.read_csv('data/DataSaurusDozen.tsv', delimiter = '\t')

alt.Chart(datasaurus[datasaurus.dataset == 'bullseye']).mark_point(color=dark2_colours[0]).encode(
    x = 'x:Q',
    y = 'y:Q',
    size = alt.value(90),
    strokeWidth = alt.value(4)
).configure_axis(
    labelFontSize = axis_label_font_size,
    titleFontSize = axis_title_font_size 
).properties(
    height = 600,
    width = 600
).save('big_bullseye.json')
