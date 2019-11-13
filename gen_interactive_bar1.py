import pandas as pd
import altair as alt

from config import color_scale_scheme, axis_label_font_size, axis_title_font_size, axis_title_font_size2


df = pd.read_csv('data/scale_responses.csv')

df.Chart(df).mark_bar().encode(
).transform_calculate(

