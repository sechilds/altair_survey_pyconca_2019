import altair as alt
from vega_datasets import data

source = data.cars()

brush = alt.selection(type='interval')

points = alt.Chart(source).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color=alt.condition(brush, alt.Color('Origin:N', scale = alt.Scale(scheme = 'dark2')), alt.value('lightgray'))
).properties(
        width=800,
        height=300
).add_selection(
    brush
)

bars = alt.Chart(source).mark_bar().encode(
    y='Origin:N',
    color='Origin:N',
    x='count(Origin):Q'
).properties(
        width=800,
        height=110
).transform_filter(
    brush
)

(points & bars).configure_axis(
        labelFontSize = 24,
        titleFontSize = 36
        ).save('selection_histogram.json')

