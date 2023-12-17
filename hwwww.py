import numpy as np
import matplotlib.pyplot as plt

# Функция для визуализации (примерная функция ямы)
def terrain_function(x, y):
    return x**2 + y**2

# Генерация сетки значений для рельефа
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
x, y = np.meshgrid(x, y)
z = terrain_function(x, y)

# Функция покоординатного спуска
def coordinate_descent(start_point, func, step_size=0.09, max_iter=1000):
    path = [start_point]
    current_point = start_point

    for _ in range(max_iter):
        # Выбираем направление с наибольшим уклоном (производная по x, затем по y)
        grad_x = np.array([func(current_point[0] + step_size, current_point[1]) - func(*current_point), 0])
        grad_y = np.array([0, func(current_point[0], current_point[1] + step_size) - func(*current_point)])

        if np.linalg.norm(grad_x) > np.linalg.norm(grad_y):
            next_point = current_point - grad_x
        else:
            next_point = current_point - grad_y

        path.append(next_point)
        current_point = next_point

    return np.array(path)

# Начальная точка и выполнение покоординатного спуска
start_point = np.array([8, 8])
path = coordinate_descent(start_point, terrain_function)

# Визуализация
plt.figure(figsize=(10, 8))
plt.contourf(x, y, z, levels=50, cmap='viridis')
plt.plot(path[:, 0], path[:, 1], 'r.-') # Траектория спуска
plt.plot(start_point[0], start_point[1], 'bo') # Начальная точка
plt.title('Покоординатный спуск лыжника')
plt.xlabel('X координата')
plt.ylabel('Y координата')
plt.colorbar(label='Высота')
plt.show()
