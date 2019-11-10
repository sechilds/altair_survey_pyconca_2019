import altair as alt
from vega_datasets import data

source = data.sp500.url

brush = alt.selection(type='interval', encodings=['x'])

upper = alt.Chart(source).mark_area().encode(
    alt.X('date:T', scale=alt.Scale(domain=brush)),
    y='price:Q'
).properties(
    width=800,
    height=400)

lower = upper.properties(
    height=120
).add_selection(brush)

(upper & lower).configure_axis(
        labelFontSize = 24,
        titleFontSize = 36).save('interval_selection.json')

