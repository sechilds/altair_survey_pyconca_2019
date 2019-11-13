import pandas as pd

df = pd.read_csv('data/diverging_bar_chart_data.csv')

df = df[['field_name', 'response', 'count', 'freq', 'Gender', 'Customer Type', 'Type of Travel', 'Class']]

table_html = df.to_html(max_rows=8, max_cols=8)

with open('aggregatged_survey_data.html', 'w') as f:
    f.write(table_html)
