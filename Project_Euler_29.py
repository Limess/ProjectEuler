L=set()
for a in range (2, 101):
    for b in range (2, 101):
        L.add(a**b)
print(len(L))
