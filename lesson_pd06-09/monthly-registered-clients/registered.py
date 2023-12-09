def solve():
    df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')
    registered_clients = df.groupby(df['date'].dt.month).size().reset_index(name='clients')
    registered_clients = registered_clients.rename(columns={'date': 'month'})
    registered_clients = registered_clients.set_index('month')


    print(registered_clients)