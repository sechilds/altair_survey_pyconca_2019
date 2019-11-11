import pandas as pd

df = pd.read_excel('data/customer-satisfaction/satisfaction.xlsx')

table_html = df.to_html(max_rows=8, max_cols=6)

with open('raw_survey_data.html', 'w') as f:
    f.write(table_html)
