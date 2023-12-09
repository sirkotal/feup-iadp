def solve():
    res = df.groupby(['class', 'sex']).agg(
        max_age=('age', 'max'),
        min_weight=('weight', 'min'),
        mean_height=('height', 'mean')
    ).reset_index()

    res['mean_height'] = res['mean_height'].round(2)

    res = res.set_index(['class', 'sex']).sort_index(level=0)

    print(res)