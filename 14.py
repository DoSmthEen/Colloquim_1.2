"""
Сформуйте лінійний масив дійсних чисел, елементи якого є відстанями,
пройденими тілом при вільному падінні на землю за 1, 2, ..., 10 с.
Васильченко Даниїл Назарович 122А
"""
import numpy as np

# Введення массиву
input_massive = np.array([(9.8 * i) for i in range(1,  11)])

# Виведення масиву
print("Ваш масив: ", input_massive)