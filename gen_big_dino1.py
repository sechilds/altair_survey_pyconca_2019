import pandas as pd
import altair as alt

def my_theme():
    return {
            'config': {
                'range': {'category': {'scheme': 'dark2'}}
            }
        }

alt.themes.register('my_theme', my_theme)
alt.themes.enable('my_theme')

datasaurus = pd.read_csv('data/DataSaurusDozen.tsv', delimiter = '\t')

alt.Chart(datasaurus[datasaurus.dataset == 'dino']).mark_point(color="#1b9e77").encode(
    x = 'x:Q',
    y = 'y:Q',
    size = alt.value(90),
    strokeWidth = alt.value(4)
).configure_axis(
    labelFontSize = 24,
    titleFontSize = 36
).properties(
    height = 600,
    width = 600
).save('slide1.json')
