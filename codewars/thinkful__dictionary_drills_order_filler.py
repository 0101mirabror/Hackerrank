def fillable(stock, merch, n):
    return True if stock[merch] >= n else False

stock = {
            'football': 4,
            'boardgame': 10,
            'leggos': 1,
            'doll': 5 }