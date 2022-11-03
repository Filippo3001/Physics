import numpy as np
from matplotlib import pyplot as plt

# in MeV
a_v = 15.5
a_s = 16.8
a_l = 0.72
a_a = 23.0
a_p = 34.0


class Nucleus:
    def __init__(self, a, z):
        self.A = a
        self.Z = z

    def alpha(self):
        self.A -= 4
        self.Z -= 2

    def betaminus(self):
        self.Z += 1

    def betaplus(self):
        self.Z -= 1



def delta(nuc):
    if (nuc.A - nuc.Z) % 2 == 0 & nuc.Z % 2 == 0:
        return 1
    if (nuc.A - nuc.Z) % 2 != 0 & nuc.Z % 2 != 0:
        return -1
    else:
        return 0


def B(nuc):
    return a_v * nuc.A - a_s * (nuc.A ** (2 / 3)) - a_l * (nuc.Z * (nuc.Z - 1) / (nuc.A ** (1 / 3))) - a_a * (
            (nuc.A - 2 * nuc.Z) ** 2) / nuc.A + a_p * delta(nuc) / (nuc.A ** (3 / 4))


def is_alpha(nuc):
    if nuc.A < 4 or nuc.Z < 2:
        return 1  # false
    if B(nuc) > B(nuc.alpha()):
        return 1  # false
    else:
        return 0  # true


z = 49  # fisso z

a = np.arange(96, 137)
B_on_A_values = []
for x in a:
    nuc = Nucleus(x, z)
    B_on_A_values.append(B(nuc) / x)

plt.plot(a, B_on_A_values, "o")
plt.show()
