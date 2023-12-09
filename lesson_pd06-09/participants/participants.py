def solve():
    res = pd.pivot_table(df, index='city', columns='class', values='name', aggfunc='count', margins=True,
                            margins_name='All')
    print(res)