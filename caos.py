from classes import Chaos
import matplotlib.pyplot as plt

ch = Chaos(0.1, 4.0)
ts5 = ch.generate_sequence(5)

print(ts5)

ch = Chaos(0.1, 4.0)
ts_length = 250

fig, ax = plt.subplots()
ax.set_xlabel('$t$', fontsize=14)
ax.set_ylabel('$x_t$', fontsize=14)
x = ch.generate_sequence(ts_length)
ax.plot(range(ts_length), x, 'bo-', alpha=0.5, lw=2, label='$x_t$')
plt.show()

# bifurcation diagram

fig, ax = plt.subplots()
ch = Chaos(0.1, 4)
r = 2.5
while r < 4:
    ch.r = r
    t = ch.generate_sequence(1000)[950:]
    ax.plot([r] * len(t), t, 'b.', ms=1)
    r = r + 0.005

ax.set_xlabel('$r$', fontsize=16)
plt.show()
