# gen_dashboard1.py
import pandas as pd
import altair as alt

df = pd.read_csv('data/diverging_bar_chart_data.csv')

gender_radio = alt.binding_radio(options = list(df['Gender'].unique()))
class_dropdown = alt.binding_select(options = list(df['Class'].unique()))
customer_type_dropdown = alt.binding_select(options = list(df['Customer Type'].unique()))
travel_type_dropdown = alt.binding_select(options = list(df['Type of Travel'].unique()))

gender_selection = alt.selection_single(bind=gender_radio, fields=['Gender'])
class_selection = alt.selection_single(bind=class_dropdown, fields=['Class'])
customer_type_selection = alt.selection_single(bind=customer_type_dropdown, fields=['Customer Type'])
travel_type_selection = alt.selection_single(bind=travel_type_dropdown, fields=['Type of Travel'])

alt.Chart(df).mark_bar().encode(
        x = 'start_percent:Q',
        x2 = 'end_percent:Q',
        y = alt.Y('field_name:N', sort = alt.EncodingSortField(field = 'percent_positive', op = 'min', order = 'ascending')),
        color = alt.Color('response:N', scale = alt.Scale(scheme = 'dark2'))
).add_selection(
        gender_selection,
        class_selection,
        customer_type_selection,
        travel_type_selection).transform_filter(
        gender_selection).transform_filter(
        class_selection).transform_filter(
        customer_type_selection).transform_filter(
        travel_type_selection).save('dashboard1.json')


