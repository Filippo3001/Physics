import numpy as np
from matplotlib import pyplot as plt

# in MeV
a_v = 15.5
a_s = 16.8
a_l = 0.72
a_a = 23.0
a_p = 34.0


def delta(A, Z):
    if A % 2 == 0 & Z % 2 == 0:
        return 1
    if A % 2 != 0 & Z % 2 != 0:
        return -1
    else:
        return 0


def B(A, Z):
    return a_v*A - a_s*(A**(2/3)) - a_l*(Z*(Z-1)/(A**(1/3))) - a_a*((A- 2*Z)**2)/A + a_p*delta(A,Z)/(A**(3/4))

z = 26 # fisso z

a = np.arange(45, 70)
B_on_A_values = []
for x in  a:
    B_on_A_values.append(B(x,z)/x)

plt.plot(a, B_on_A_values, "o")
plt.show()

