def solve():
    avg = df.groupby('class')['age'].mean()
    avg = avg.rename('avg age').round(2).reset_index()
    avg = avg.set_index('class')


    print(avg)