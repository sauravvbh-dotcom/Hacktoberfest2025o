# Your code here
n, a, b, c = map(int, input().split())

cycle = a + b + c
total = 0
day = 0


if n >= cycle:
    full_cycles = n // cycle
    total = full_cycles * cycle
    day = full_cycles * 3


while total < n:
    day += 1
    if day % 3 == 1:
        total += a
    elif day % 3 == 2:
        total += b
    else:
        total += c

print(day)
