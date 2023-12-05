def solve():
    max_pilates = df[df['class'] == 'pilates']['hours'].idxmax()

    name = df.loc[max_pilates, 'name']

    print(name)