import numpy as np

# Из списка
list1 = [10, 20, 30, 40, 50]
ar = np.array(list1)
print(ar)

array_from_list = np.array([1, 2, 3, 4, 5])
print(array_from_list)  # [1 2 3 4 5]

# Из кортежа
array_from_tuple = np.array((1, 2, 3, 4, 5))
print(array_from_tuple)  # [1 2 3 4 5]

# Массив из нулей
zeros_array = np.zeros((3, 4))  # 3 строки, 4 столбца
print(zeros_array)

# Массив из единиц
ones_array = np.ones((2, 5))    # 2 строки, 5 столбцов
print(ones_array)

# Массив 3x3, заполненный числом 7
full_array = np.full((3, 3), 7)
print(full_array)

# Массив от 0 до 9
arange_array = np.arange(10)
print(arange_array)  # [0 1 2 3 4 5 6 7 8 9]

# Массив с шагом 2
arange_step_array = np.arange(0, 20, 2)  # от 0 до 20 с шагом 2
print(arange_step_array)  # [ 0  2  4  6  8 10 12 14 16 18]

# Массив случайных чисел от 0 до 1
random_array = np.random.rand(3, 4)  # 3 строки, 4 столбца
print(random_array)

# Массив случайных целых чисел
random_int_array = np.random.randint(0, 10, (3, 3))  # от 0 до 10, размер 3x3
print(random_int_array)

# Массив из 5 чисел, равномерно распределенных между 0 и 1
linspace_array = np.linspace(0, 1, 5)
print(linspace_array)



