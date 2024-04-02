def usdcny(usd):
    a = f'{usd*6.75}00'.split('.')
    return f'{a[0]}.{a[1][:2]}'
print(usdcny(4))