import pandas as pd
import altair as alt

anscombe = pd.read_csv('data/anscombes.csv')

alt.Chart(anscombe).mark_point().encode(
    x = 'x:Q',
    y = 'y:Q',
    color = alt.Color('dataset:N', scale = alt.Scale(scheme = 'dark2'))
).facet(
    facet='dataset:N',
    columns = 2).save('anscombe_all.json').properties(
            height = 600,
            width = 800
