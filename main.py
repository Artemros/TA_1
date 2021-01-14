import matplotlib.pyplot as plt
import numpy as np
from histogram import Histogram
import distributions as dst

graph_disc = 200
ns = [10, 50, 1000]
ds = dst.get_distributions()

for d in ds:
    for n in ns:
        data = [d.x() for i in range(n)]
        hs = Histogram(data, d.discrete())
        x = np.linspace(min(data), max(data), graph_disc)
        yf = [d.f(k) for k in x]
        yF = [d.F(k) for k in x]
        plt.subplot(2, len(ns), ns.index(n) + 1)
        plt.title(d.name + ", n = " + str(n))
        plt.xlabel('normalNumbers')
        plt.ylabel('Density')
        plt.plot(x, yf, label='expected')
        plt.step(hs.x, hs.y, label='received')
        plt.legend()
        plt.subplot(2, len(ns), ns.index(n) + len(ns) + 1)
        plt.xlabel('x')
        plt.ylabel('F(x)')
        plt.plot(x, yF, label='expected')
        plt.step(hs.x, hs.F(), label='received')
        plt.legend()
    plt.show()
