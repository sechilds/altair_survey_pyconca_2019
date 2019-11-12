# gen_dashboard2.py
import pandas as pd
import altair as alt

df = pd.read_csv('data/diverging_bar_chart_data.csv')

gender_radio = alt.binding_radio(options = list(df['Gender'].unique()), name = 'Gender')
class_dropdown = alt.binding_select(options = list(df['Class'].unique()), name = 'Class')
customer_type_dropdown = alt.binding_select(options = list(df['Customer Type'].unique()), name = 'Customer Type')
travel_type_dropdown = alt.binding_select(options = list(df['Type of Travel'].unique()), name = 'Type of Travel')

gender_selection = alt.selection_single(bind=gender_radio, fields=['Gender'], init={'Gender': 'Female'})
class_selection = alt.selection_single(bind=class_dropdown, fields=['Class'], init={'Class': 'Eco'})
customer_type_selection = alt.selection_single(bind=customer_type_dropdown, fields=['Customer Type'], init={'Customer Type': 'All'})
travel_type_selection = alt.selection_single(bind=travel_type_dropdown, fields=['Type of Travel'], init={'Type of Travel': 'All'})

base = alt.Chart(df).encode(
        y = alt.Y('field_name:N', sort = alt.EncodingSortField(field = 'percent_positive', op = 'min', order = 'ascending')),
        tooltip = [alt.Tooltip('count:Q', title = 'Count of Records'),
            alt.Tooltip('freq:Q', title = 'Percentage'),
            alt.Tooltip('field_name:N', title = 'Question'),
            alt.Tooltip('response:Q', title = 'Answer')]
).transform_filter(
gender_selection).transform_filter(
class_selection).transform_filter(
customer_type_selection).transform_filter(
travel_type_selection
)

level1 = base.mark_bar().encode(
        x = 'start_percent:Q',
        x2 = 'end_percent:Q',
        color = alt.Color('response:N', scale = alt.Scale(scheme = 'dark2'))
).add_selection(
        gender_selection,
        class_selection,
        customer_type_selection,
        travel_type_selection)

level2 = base.mark_text().encode(
        x = 'midpoint_percent:Q',
        text = alt.Text('freq:Q', format = '.2%')
)

(level1 + level2
).add_selection(
        gender_selection,
        class_selection,
        customer_type_selection,
).save('dashboard2.json')





