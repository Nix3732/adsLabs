from typing import List, Tuple
import math
import random

Point = Tuple[int, int]


def are_collinear(a: Point, b: Point, c: Point, tolerance: float = 1e-9) -> bool:
    area = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return math.isclose(area, 0.0, abs_tol=tolerance)


def has_non_collinear_triple(points: List[Point]) -> bool:

    n = len(points)
    if n < 3:
        return False

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if not are_collinear(points[i], points[j], points[k]):
                    return True
    return False

def calculate_polar_angle(ref: Point, point: Point):        #Вычисление полярного угла между начальной и опорной точкой
    return math.atan2(point[1] - ref[1], point[0] - ref[0])


def calculate_cross_product(o: Point, a: Point, b: Point):         #Вычисление векторного произведения
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def find_convex_hull(points: List[Point]) -> List[Point]:     #Алгоритм Грэхема
    start_point = min(points, key=lambda p: (p[1], p[0]))    #Начальная точка

    sorted_points = sorted(                                  #Сортировка по полярному углу и расстоянию
        [p for p in points if p != start_point],
        key=lambda p: (calculate_polar_angle(start_point, p),
                       (p[0] - start_point[0]) ** 2 + (p[1] - start_point[1]) ** 2))

    hull = [start_point, sorted_points[0]]   #Стэк

    for current_point in sorted_points[1:]:      #Внутренняя оболочка
        while len(hull) > 1 and calculate_cross_product(hull[-2], hull[-1], current_point) <= 0:
            hull.pop()
        hull.append(current_point)

    return hull


#Создание случайных чисел
def generate_random_points(num_points: int, coord_range: Tuple[int, int] = (-1000, 1000)) -> List[Point]:
    points = []
    while len(points) < num_points:
        new_point = (random.randint(*coord_range), random.randint(*coord_range))
        if new_point not in points:  # Избегаем дубликатов
            points.append(new_point)
    return points


def get_user_points():           #Получение точек пользователя
    while True:
        points = []
        for i in range(num_points):
            coords = input(f"Введите координаты точки {i + 1} (x, y): ").split()
            if len(coords) != 2:
                print("Нужно ровно 2 числа!")
                break
            x, y = map(int, coords)
            points.append((x, y))

        return points


def print_points(points: List[Point]):
    for i, point in enumerate(points, 1):
        print(f"{i}. ({point[0]}, {point[1]})")


print("1. Сгенерировать случайные точки")
print("2. Ввести точки вручную")

while True:
    choice = input("Ваш выбор: ")
    if choice not in ('1', '2'):
        print("Введите 1 или 2")
        continue

    try:
        if choice == '1':
            num_points = int(input("Введите количество случайных точек (минимум 3): "))
            if num_points < 3:
                print("Нужно минимум 3 точки!")
                break
            points = generate_random_points(num_points)
            if not has_non_collinear_triple(points):
                print("Все точки лежат на одной прямой. Введите другие числа")
                break
            print("\nСгенерированные точки:")
            print_points(points)
        else:
            num_points = int(input("Введите количество случайных точек (минимум 3): "))
            if num_points < 3:
                print("Нужно минимум 3 точки!")
                break
            points = get_user_points()
            if not has_non_collinear_triple(points):
                print("Все точки лежат на одной прямой")
                break
            print_points(points)

        convex_hull = find_convex_hull(points)
        print("\nВыпуклая оболочка состоит из точек:")
        print_points(convex_hull)
        break

    except ValueError as e:
        print(f"\nОшибка: {e}")
        if choice == '1':
            print("Попробуйте снова с другим количеством точек.")
        else:
            print("Попробуйте ввести точки снова.")
