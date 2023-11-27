def solve():
    df['bmi'] = df['weight'] / ((df['height'] / 100) ** 2)
    df['bmi'] = df['bmi'].round(2)

    print(df[['id', 'name', 'weight', 'height', 'bmi']].head(3))