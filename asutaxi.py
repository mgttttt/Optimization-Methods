import math
import matplotlib.pyplot as plt

x1, x2, z1, z2, c1, c2 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0


def f(x):
    return math.sqrt((x - x1) ** 2 + z1 ** 2) / c1 + math.sqrt((x - x2) ** 2 + z2 ** 2) / c2


def derivative(x):
    return (x - x1) / (math.sqrt((x - x1) ** 2 + z1 ** 2) * c1) + (x - x2) / (math.sqrt((x - x2) ** 2 + z2 ** 2) * c2)


def gradient_descent(initial_x, learning_rate, num_iterations):
    x = initial_x

    for i in range(num_iterations):
        gradient = derivative(x)
        x = x - learning_rate * gradient

    return x


if __name__ == "__main__":
    x1, z1 = map(float, input("Введите координаты человека на песке (x1, z1): ").split())
    x2, z2 = map(float, input("Введите координаты человека в воде (x2, z2): ").split())
    c1 = float(input("Введите скорость передвижения на песке (c1): "))
    c2 = float(input("Введите скорость передвижения на воде (c2): "))

    initial_x = x1 if x1 <= x2 else x2
    learning_rate = 0.01
    num_iterations = 100

    result = gradient_descent(initial_x, learning_rate, num_iterations)

    print(f"Минимумальное значение функции: {f(result)}")
    print(f"Значение x: {result}")
    fig, ax = plt.subplots()
    x = [x1, result, x2]
    y = [z1, 0, z2]
    plt.axhline(y=0)
    #ax.plot(x, y, 'ro')
    plt.plot(x, y, marker="o", c="g")
    plt.show()
