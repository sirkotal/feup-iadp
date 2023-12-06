import numpy

def solve():
    table = pd.pivot_table(df, index=['city', 'sex'], columns='rank', aggfunc='size', fill_value=0)

    formatted_table = table.applymap(lambda x: f'{x:.1f}' if x != 0 else numpy.nan)

    print(formatted_table)
