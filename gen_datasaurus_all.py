import pandas as pd
import altair as alt

datasaurus = pd.read_csv('data/DataSaurusDozen.tsv', delimiter = '\t')

alt.Chart(datasaurus).mark_point().encode(
    x = 'x:Q',
    y = 'y:Q',
    size = alt.value(90),
    strokeWidth = alt.value(4),
    color = alt.Color('dataset:N',
        scale = alt.Scale(scheme = 'dark2')),
    fill = alt.Fill('dataset:N',
        scale = alt.Scale(scheme = 'dark2')),
    stroke = alt.Stroke('dataset:N',
        scale = alt.Scale(scheme = 'dark2'))
    ).properties(
            height = 130,
            width = 100).facet('dataset:N', columns = 3).save('datasaurus_all.json')
