from typing import Tuple
import math
import random
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

Point = Tuple[int, int]


def are_collinear(a, b, c):                  #Проверка коллиниарности
    return math.isclose((b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]), 0)


def point_in_triangle(p, triangle, include_boundary):
    a, b, c = triangle
    #Вычисление ориентаций с помощью векторных произведений
    d1 = (p[0] - b[0]) * (a[1] - b[1]) - (a[0] - b[0]) * (p[1] - b[1])
    d2 = (p[0] - c[0]) * (b[1] - c[1]) - (b[0] - c[0]) * (p[1] - c[1])
    d3 = (p[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (p[1] - a[1])

    if not include_boundary:
        has_neg = (d1 <= 0) or (d2 <= 0) or (d3 <= 0)
        has_pos = (d1 >= 0) or (d2 >= 0) or (d3 >= 0)
    else:
        has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
        has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

    return not (has_neg and has_pos)                          #Внутри если нет и той и той ориентации


def find_nested_triangles(points):                              #Нахождение вложенных треугольников
    n = len(points)
    if n < 6:
        return None

    triangles = []                                              #Создание всех треугольников
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if not are_collinear(points[i], points[j], points[k]):
                    triangles.append((points[i], points[j], points[k]))

    triangles.sort(key=lambda t: abs(                           #Сортируем по площади
        (t[1][0] - t[0][0]) * (t[2][1] - t[0][1]) - (t[1][1] - t[0][1]) * (t[2][0] - t[0][0])
    ))

    for i in range(len(triangles)):                             #Перебираем все треугольники
        for j in range(i + 1, len(triangles)):
            t1 = triangles[i]
            t2 = triangles[j]

            #Все ли точки t1 внутри t2
            if all(point_in_triangle(p, t2, include_boundary=False) for p in t1):
                return t1, t2

    return None


#Генератор случайных точек
def generate_random_points(num_points, x_range, y_range):
    return [(random.randint(x_range[0], x_range[1]), random.randint(y_range[0], y_range[1]))
            for _ in range(num_points)]


def plot_triangles(points, t1, t2):
    fig, ax = plt.subplots(figsize=(10, 10))
    x, y = zip(*points)
    ax.scatter(x, y, color='blue', label='Точки')

    #Точки
    for i, (px, py) in enumerate(points):
        ax.text(px, py, f'{i}', fontsize=11, ha='right')

    #Внешний треугольник
    t2_poly = Polygon(t2, closed=True, fill=False, color='red', linewidth=2, label='Внешний треугольник')
    ax.add_patch(t2_poly)

    #Внутренний треугольник
    t1_poly = Polygon(t1, closed=True, fill=False, color='green', linewidth=2, label='Внутренний треугольник')
    ax.add_patch(t1_poly)

    ax.set_title('Вложенные треугольники')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()
    ax.grid(True)
    plt.show()


points = generate_random_points(20, (0, 100), (0, 100))  #Точки в квадрате 100*100
# points = [
#     (0, 0), (2, 0), (1, 2),
#     (1, 0), (0.5, 1), (1.5, 1)
# ]
print("Сгенерированные точки:")
for i, p in enumerate(points):
    print(f"{i + 1}: {p}")

result = find_nested_triangles(points)

if result:
    t1, t2 = result
    print("\nНайдены вложенные треугольники:")
    print(f"Внутренний: {t1}")
    print(f"Внешний: {t2}")
    plot_triangles(points, t1, t2)
else:
    print("\nВложенные треугольники не найдены")

    fig, ax = plt.subplots(figsize=(10, 10))
    x, y = zip(*points)
    ax.scatter(x, y, color='blue', label='Точки')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)
    plt.show()
