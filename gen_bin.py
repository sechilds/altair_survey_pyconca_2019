import altair as alt
from vega_datasets import data
from config import dark2_colours, axis_label_font_size, axis_title_font_size

movies = data.movies()


alt.Chart(movies).mark_bar(color=dark2_colours[0]).encode(
        alt.X("IMDB_Rating:Q", bin=True),
        y='count()',
).configure_axis(
        labelFontSize = axis_label_font_size,
        titleFontSize = axis_title_font_size
).properties(
        height = 400,
        width = 400
).save('bin.json')
