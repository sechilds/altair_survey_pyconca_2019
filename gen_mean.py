import altair as alt
from vega_datasets import data
from config import dark2_colours, axis_label_font_size, axis_title_font_size

cars = data.cars()

alt.Chart(cars).mark_bar(color=dark2_colours[1]).encode(
        y='Cylinders:O',
        x='mean(Acceleration):Q'
).configure_axis(
        labelFontSize = axis_label_font_size,
        titleFontSize = axis_title_font_size
).properties(
        height = 400,
        width = 400
).save('mean.json')
