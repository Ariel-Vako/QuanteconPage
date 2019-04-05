import numpy as np
import matplotlib.pyplot as plt
from classes import Market, deadw

baseline_params = 15, 0.5, -2, 0.5, 3
m = Market(*baseline_params)

q_max = m.quantity() * 2
q_grid = np.linspace(0.0, q_max, 100)
pd = m.inverse_demand(q_grid)
ps = m.inverse_supply(q_grid)
psno = m.inverse_supply_no_tax(q_grid)

fig, ax = plt.subplots()
ax.plot(q_grid, pd, lw=2, alpha=0.6, label='demanda')
ax.plot(q_grid, ps, lw=2, alpha=0.6, label='oferta')
ax.plot(q_grid, psno, '--k', lw=2, alpha=0.6, label='Oferta sin impuestos')
ax.set_xlabel('Cantidad', fontsize=14)
ax.set_xlim(0, q_max)
ax.set_ylabel('Precio', fontsize=14)
ax.legend(loc='lower right', frameon=False, fontsize=14)
plt.show()

baseline_params = 15, 0.5, -2, 0.5, 3
m = Market(*baseline_params)
peso = deadw(m)
print(peso)
