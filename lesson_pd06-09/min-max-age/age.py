def solve():
    result = df.groupby('class')['age'].agg(min_age='min', max_age='max',
                                            mean_age=('age', lambda x: round(x.mean(), 2)))

    print(result)