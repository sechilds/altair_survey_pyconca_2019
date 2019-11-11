import pandas as pd

df = pd.read_csv('data/scale_responses.csv')

table_html = df.to_html(max_rows=8, max_cols=6)

with open('transformed_survey_data.html', 'w') as f:
    f.write(table_html)
