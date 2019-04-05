from random import uniform
from classes import ECDF

samples = [uniform(0, 1) for i in range(10)]
F = ECDF(samples)
print(F(0.5))

F.observations = [uniform(0, 1) for i in range(1000)]
print(F(0.5))
