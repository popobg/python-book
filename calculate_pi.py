"""Calculate pi with the Nilakantha series"""

def increment_2(dn):
    dn += 2
    return dn

sign = 1
dn1 = 2
dn2 = 3
dn3 = 4
p = 3.0

n = int(input("Combien de fois ?\n> "))

for i in range(1, n + 1):
    p = p + sign * (4/(dn1 * dn2 * dn3))
    dn1 = increment_2(dn1)
    dn2 = increment_2(dn2)
    dn3 = increment_2(dn3)
    sign = -sign

print(p)