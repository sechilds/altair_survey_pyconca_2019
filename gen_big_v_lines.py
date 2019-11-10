import pandas as pd
import altair as alt

datasaurus = pd.read_csv('data/DataSaurusDozen.tsv', delimiter = '\t')

alt.Chart(datasaurus[datasaurus.dataset == 'v_lines']).mark_point(color="#1b9e77").encode(
    x = 'x:Q',
    y = 'y:Q',
    size = alt.value(90),
    strokeWidth = alt.value(4)
).configure_axis(
    labelFontSize = 24,
    titleFontSize = 36
).properties(
    height = 600,
    width = 600
).save('big_v_lines.json')
