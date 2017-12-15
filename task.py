from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

n = 20
Xn = np.random.normal(size = n)

a0 = 0
a1 = 1
sig = 1
m = np.mean(Xn)

norm0 = norm(loc=a0, scale=sig/np.sqrt(n))
norm1 = norm(loc=a1, scale=sig/np.sqrt(n))

x = np.linspace(norm0.ppf(0.01),norm1.ppf(0.99), 100)

plt.plot(x, norm0.sf(x),'b-', label= 'First type error probability')
plt.plot(x, norm1.cdf(x),'r-',  label='Second type error probability')
plt.plot(m, norm0.sf(m), 'go')
plt.plot(m, norm1.cdf(m), 'go')
plt.legend(frameon=False)
plt.xlabel(r'$\overline{X_n}$')
plt.ylabel('Probability')
plt.show()
