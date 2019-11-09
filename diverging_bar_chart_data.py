import pandas as pd
from itertools import combinations, chain

def diverging_scale_data(df, group_fields = []):
    group_fields.append('field_name')
    counts = df.groupby(group_fields + ['response'])['satisfaction_v2'].count()
    freq = counts.groupby(level=list(range(0, len(group_fields)))).apply(lambda x : x / float(x.sum()))
    counts = pd.concat([counts, freq], axis = 1)
    counts.columns = ['count', 'freq']
    counts = counts.reset_index()
    counts['negative'] = counts['response'].apply(lambda x : True if x < 3 else False)
    counts['end_percent'] = counts.groupby(group_fields)['freq'].cumsum()
    counts['start_percent'] = counts.groupby(group_fields)['end_percent'].shift(1).fillna(0)
    negative_pct_size = counts[counts.negative].groupby(group_fields)['freq'].sum()
    # midpoint_pct_size = counts[counts.response == 3].groupby(group_fields)['freq'].sum()
    # starting_point = negative_pct_size.add((midpoint_pct_size / 2), fill_value=0.0)
    starting_point = negative_pct_size
    starting_point = pd.DataFrame(starting_point).reset_index()
    starting_point.columns = group_fields + ['starting_point']
    counts = pd.merge(counts, starting_point, on = group_fields, how = 'left')
    counts['end_percent'] = counts['end_percent'] - counts['starting_point']
    counts['start_percent'] = counts['start_percent'] - counts['starting_point']
    counts['midpoint_percent'] = counts['start_percent'] + (counts['freq'] / 2.0)
    counts['percent_positive'] = 1 - counts['starting_point']
    counts = counts[group_fields + ['response', 'count', 'freq', 'start_percent', 'end_percent', 'midpoint_percent', 'percent_positive']]
    return counts

def all_combinations(any_list):
    return chain.from_iterable(
            combinatiosn(any_list, i) for i in range(len(any_list) +1))

filters = ['Gender', 'Customer Type', 'Type of Travel', 'Class']

df = pd.read_csv('data/scale_responses.csv')

combos = (diverging_scale_data(df, group_fields = list(i)) for i in all_combinations(filters))
combos_data = pd.concat(combos, axis = 0, sort = False)
combos_data = combos_data.fillna('All')

combos_data.to_csv('data/diverging_bar_chart_data.csv')

