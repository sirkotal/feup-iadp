def solve():
    df['date'] = pd.to_datetime(df['date'])
    filtered_df = df[df['date'].dt.year > 2014]

    table = pd.pivot_table(filtered_df, index='status', columns='sex', aggfunc='size', fill_value='NaN')
    formatted_table = table.applymap(lambda x: f'{x:.1f}' if isinstance(x, float) else x)

    print(formatted_table)