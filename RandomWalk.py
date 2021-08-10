from random import choice

class RandomWalk():
    """Класс для генерирования случайных блужданий"""
    def __init__(self, num_point=5000):
        self.num_points = num_point
        self.x_values = [0]
        self.y_values = [0]

    """Вычисляет все точки блуждания."""
    def fill_walk(self): 
        # Шаги генерируются до достижения нужной длины.
        while len(self.x_values) < self.num_points:
            # Определение направления и длины перемещения.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            
            # Отклонение нулевых перемещений.
            if x_step == 0 and y_step == 0:
                continue
            
            # Вычисление следующих значений x и y.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)
    