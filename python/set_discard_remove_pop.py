n = int(input())
s = set(map(int, input().split()))
"discard va remove ikkalasi ham set va listdan elementni olib tashlaydi, discardda element topilmasa error bermay bajariladi, removeda element topilmasa error beradi"
for i in range(int(input())):
    command = input()
    if command.startswith('pop'):
        s.pop()
        print(s)
    elif command.startswith('remove'):
        s.remove(int(command.split()[1]))
        print(s)
    elif command.startswith('discard'):
        s.discard(int(command.split()[1]))
        print(s)

print((sum(s)))