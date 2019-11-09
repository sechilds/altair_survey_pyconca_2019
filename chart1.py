import pandas as pd
import altair as alt

datasaurus = pd.read_csv('data/DataSaurusDozen.tsv', delimiter = '\t')

alt.Chart(datasaurus).mark_point().encode(
    x = 'x:Q',
    y = 'y:Q',
    size = alt.value(90),
    strokeWidth = alt.value(4)
).transform_filter(alt.datum.dataset == 'dino').configure_axis(
    labelFontSize = 24,
    titleFontSize = 36
).properties(
    height = 800,
    width = 800
).save('slide1.html')
