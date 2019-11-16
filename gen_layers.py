import altair as alt
from vega_datasets import data
from config import color_scale_scheme, axis_label_font_size, axis_title_font_size, axis_title_font_size2, axis_title_font_size3

source = data.movies()

heatmap = alt.Chart(source).mark_rect().encode(
    alt.X('IMDB_Rating:Q', bin=True, axis = alt.Axis(title = 'IMDB')),
    alt.Y('Rotten_Tomatoes_Rating:Q', bin=True, axis = alt.Axis(title = 'Rotten Tomatoes')),
    alt.Color('count()', scale=alt.Scale(scheme='darkgreen'))
)

points = alt.Chart(source).mark_circle(
    color='white',
    size=25,
).encode(
    x=alt.X('IMDB_Rating:Q', axis = alt.Axis(title = 'IMDB')),
    y=alt.Y('Rotten_Tomatoes_Rating:Q', axis = alt.Axis(title = 'Rotten Tomatoes')),
    tooltip=['Title:N',
        alt.Tooltip('Release_Date:N', title = 'Release Date'),
        alt.Tooltip('US_Gross:Q', title = 'US Gross'),
        alt.Tooltip('Worldwide_Gross:Q', title = 'Worldwide Gross')]
)

(heatmap + points
).properties(
        height = 600,
        width = 300
).configure_axis(
        labelFontSize = axis_label_font_size,
        titleFontSize = axis_title_font_size3
).save('layers.json')
