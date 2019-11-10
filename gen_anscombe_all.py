import pandas as pd
import altair as alt

anscombe = pd.read_csv('data/anscombes.csv')

alt.Chart(anscombe).mark_point().encode(
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
            height = 200,
            width = 300).facet('dataset:N', columns = 2).save('anscombe_all.json')
