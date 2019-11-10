import pandas as pd
import altair as alt

df = pd.read_excel('data/customer-satisfaction/satisfaction.xlsx')

uc = df.nunique().reset_index()
uc.columns = ['field', 'count']
alt.Chart(uc).mark_bar().encode(
        y=alt.Y('field:N',
            sort=alt.EncodingSortField(field='count', order = 'descending'),
            axis=alt.Axis(labelPadding=25, labelLimit=350, titlePadding=75)),
        x='count:Q'
).configure_axis(
        labelFontSize = 24,
        titleFontSize = 36
).properties(
        height = 600,
        width = 600
).transform_filter(alt.datum.count < 1000).save('unique_count2.json')
