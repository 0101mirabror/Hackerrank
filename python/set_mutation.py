n = int(input())
# s = set(map(int, input().split()))
s = set(input().split())
for i in range(int(input())):
    command = input()
    if command.startswith('intersection_update'):
        s1 = set((input().split()[:int(command.split()[1])]))
        s.intersection_update(s1)
        print(s)
    elif command.startswith('symmetric_difference_update'):
        s1 = set((input().split()[:int(command.split()[1])]))
        s.symmetric_difference_update(s1)
        print(s)
    elif command.startswith('update'):
        s1 = set((input().split()[:int(command.split()[1])]))
        s.update(s1)
    elif command.startswith('difference_update'):
        s1 = set((input().split()[:int(command.split()[1])]))
        s.difference_update(s1)
        print(s)

print(sum(set(map(int, s))))