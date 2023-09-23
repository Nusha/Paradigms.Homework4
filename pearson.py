import random as r

import scipy as sc

x = []
y = []
for i in range(5):
    x.append(r.randint(1, 15))
    y.append(r.randint(1, 15))

print(x, y)

corr_scipy = sc.stats.pearsonr(x, y)
print(corr_scipy)
