sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(sum)

sum = 0
n = 99
while True:
    sum += n
    n -= 2
    if n < 0:
        break
print(sum)

sum = 0
n = 99
while n > 0:
    n -= 2
    if n > 50:
        continue
    sum += n
print(sum)

