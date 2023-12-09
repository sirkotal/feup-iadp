def solve():
    count = df.groupby(['class', 'sex']).size()
    count.index = count.index.set_names(['class', 'sex'])

    print(count)
