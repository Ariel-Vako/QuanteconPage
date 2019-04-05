import matplotlib.pyplot as plt
from classes import Solow

s1 = Solow()
s2 = Solow(k=8.0)

T = 60
fig, ax = plt.subplots(figsize=(9, 6))

ax.plot([s1.steady_state()] * T, 'k-', label='steady state')

for s in s1, s2:
    lb = f'Capital series from initial state {s.k}'
    ax.plot(s.generate_sequence(T), 'o-', lw=2, alpha=0.6, label=lb)
    print(lb)

ax.legend()
plt.show()
