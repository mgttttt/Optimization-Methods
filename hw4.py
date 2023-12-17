from matplotlib import pyplot as plt
import numpy as np


def f(y, h):
    return 1 if y <= h else -1


delta_t = 0.1
v = 1 / delta_t
h = 10
initial_conditions = [h+10, h-10.2, h]
total_time = 50
t = np.arange(0, total_time, delta_t)
y_scenarios = {y0: np.full_like(t, y0) for y0 in initial_conditions}

for y0, y in y_scenarios.items():
    for i in range(1, len(t)):
        y[i] = y[i - 1] + delta_t * f(y[i - 1], h)

plt.figure(figsize=(12, 6))

for y0, y in y_scenarios.items():
    plt.plot(t, y, label=f'Начальный y(0) = {y0}')

plt.axhline(y=h, color='r', linestyle='--', label='Высота h')
plt.title('Автопилот')
plt.xlabel('Время (t)')
plt.ylabel('Высота (y(t))')
plt.legend()
plt.grid(True)
plt.show()
