import pandas as pd
import altair as alt

df = pd.read_excel('data/customer-satisfaction/satisfaction.xlsx')

uc = df.nunique().reset_index()
uc.columns = ['field', 'count']
alt.Chart(uc).mark_bar().encode(
        y='field',
        x='count').transform_filter(alt.datum.count < 50).save('unique_count3.json')