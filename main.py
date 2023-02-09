import numpy as np
import matplotlib.pyplot as plt

# перевод из списка в массив
my_list = [1, 2, 3, 4, 5]
numpy_arr = np.array(my_list)
print(numpy_arr)
print(type(numpy_arr))

new_arr = np.arange(1, 6)
print(new_arr)

arr = np.random.randint(2, 12, 5)
print(arr)
print(arr.dtype)

arr_new = np.array([1.23, 3.14, 55.2])
print(arr_new)
print(arr_new.dtype)

# создание тензера

tensor = np.random.randint(-5, 5,
                           (3, 3, 2))  # во вторых скобках заданы размеры тензора в высоту, ширину, глубину (оси X,Y,Z)
print(tensor)

print('Кол-во осей:', tensor.ndim)
print('Форма массива:', tensor.shape)
print('Кол-во значений:', tensor.size)

x = np.linspace(0, 15,
                101)  # числа равномерно распределяются в интервале от 0 до 15 (это будут первые два значения в скобках).
# а всего чисел в ряде будет 101 (третье значение в скобках)
print(x)

y = np.sin(x)
print(y)

# Отрисовка графика командой plot(), в которую переданы массивы точек для x и y
# С помощью .show() выводится график
plt.figure(figsize=(14, 7))
plt.plot(x, y, label='sin(x)', color='#4b0082', linewidth=4, marker='h', markerfacecolor='lightgreen',
         markeredgewidth=2, markersize=10, markevery=5)   #добавляем в график цвета и оформление
plt.plot(x, np.cos(x) / 2, label='cos(x)/2', linewidth=3, color='lightcoral',
         marker='D', markeredgecolor='black', markevery=5)

# plt.title('y=sin(x)')  # подписываем график сверху
plt.xlabel("Переменная X")  # подпись оси Х
plt.ylabel("Переменная Y")  # подпись оси Y

# plt.figure(figsize=(10, 5))  задаем размер графику

plt.legend()  # вставляем лейблы в график

# добавляем сетку на график
plt.grid()

plt.show()
