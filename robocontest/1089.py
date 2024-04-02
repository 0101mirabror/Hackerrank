dt = {
    0:"", 1 : 'bir', 20: 'yigirma', 30: 'o\'ttiz', 40: 'qirq', 50: 'ellik', 60: 'oltmish',
    2 : 'ikki', 70: 'yetmish', 80: 'sakson', 90: 'to\'qson', 3 : 'uch', 4 : 'to\'rt', 5 : 'besh', 6 : 'olti', 7 : 'yetti', 8 : 'sakkiz',
    9 : 'to\'qqiz', 10: 'o\'n'
}
n = int(input())
if n == 1000:
    print('ming')
elif n >= 100:
    a = n//100 #599 => 5
    b = n%100-n%100%10 #599=>90
    c = n%100%10
    print(dt[a], 'yuz', dt[b], dt[c])
elif  n < 100:
    a = n - n%10
    b = n%10
    print(dt[a], dt[b])
elif n == 1000:
    print('ming')
else:
    print(n)
    print(dt[n])
