import pandas as pd
import altair as alt

datasaurus = pd.read_csv('data/DataSaurusDozen.tsv', delimiter = '\t')

alt.Chart(datasaurus).mark_point().encode(
    x = 'x:Q',
    y = 'y:Q',
    size = alt.value(40),
    strokeWidth = alt.value(4),
    color = alt.Color('dataset:N',
        scale = alt.Scale(scheme = 'dark2')),
    fill = alt.Fill('dataset:N',
        scale = alt.Scale(scheme = 'dark2')),
    stroke = alt.Stroke('dataset:N',
        scale = alt.Scale(scheme = 'dark2'))
    ).properties(
            height = 150,
            width = 150).facet('dataset:N', columns = 5).save('datasaurus_all.json')
