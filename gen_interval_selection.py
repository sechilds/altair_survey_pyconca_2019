import altair as alt
from vega_datasets import data

source = data.sp500.url

brush = alt.selection(type='interval', encodings=['x'])

upper = alt.Chart(source).mark_area().encode(
    alt.X('date:T', scale=alt.Scale(domain=brush)),
    y='price:Q'
).properties(
    width=1200,
    height=400
)

lower = upper.properties(
    height=120
).add_selection(brush)

(upper & lower).save('interval_selection.json')

