import random

def success(proba = 0.5):
    return random.random() < proba

s = []
f = []

max = 1000000
div = max / 100
for i in range(1000000):
    if success(0.3):
        s.append(1)
    else:
        f.append(1)

print(f"{len(s) / div:.2f}%")
print(f"{len(f) / div:.2f}%")