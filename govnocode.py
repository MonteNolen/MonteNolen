oleg = []

for i in range(10**4):
    if i % 2 == 0:
        oleg.append(i)
print(*oleg)

oleg = []

print(i for i in range(10**4) if i % 2 == 0)
