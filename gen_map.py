import pandas as pd
import altair as alt

df = df = pd.read_csv('data/98-401-X2016060_eng_CSV/98-401-X2016060_English_CSV_data.csv')

change = df[df['DIM: Profile of Census Divisions (2247)']=='Population percentage change, 2011 to 2016']

change2 = change[['GEO_CODE (POR)', 'Dim: Sex (3): Member ID: [1]: Total - Sex']]
change2.columns = ['CDUID', 'Population percentage change, 2011 to 2016']


divisions = alt.topo_feature('data/canada_divisions/canada_divisions.json', 'canada_divisions')

alt.Chart(divisions).mark_geoshape().encode(
    longitude='longitude:Q',
    latitude='latitude:Q',
    color=alt.Color('Population percentage change, 2011 to 2016:Q', 
        scale = alt.Scale(scheme = 'darkmulti')),
    tooltip=[alt.Tooltip('properties.CDNAME:N', title = 'Name'),
        alt.Tooltip('properties.PRNAME:N', title = 'Province'),
        alt.Tooltip('Population percentage change, 2011 to 2016:Q')]
).transform_lookup(
    lookup='properties.CDUID',
    from_=alt.LookupData(change2, 'CDUID', ['Population percentage change, 2011 to 2016'])
).properties(
        width=900,
        height=600
).configure_axis(
        titleFontSize = 36,
        labelFontSize = 24
).configure_view(
        strokeWidth = 0
).project(
        type = 'conicEqualArea',
        rotate = [103, 0, 0]
).save('map.json')
