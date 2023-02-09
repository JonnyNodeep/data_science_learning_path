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

tensor = np.random.randint(-5, 5, (3, 3, 2)) # во вторых скобках заданы размеры тензора в высоту, ширину, глубину (оси X,Y,Z)
print(tensor)

print('Кол-во осей:', tensor.ndim)
print('Форма массива:', tensor.shape)
print('Кол-во значений:', tensor.size)


x = np.linspace(0, 15, 101) #числа равномерно распределяются в интервале от 0 до 15 (это будут первые два значения в скобках).
# а всего чисел в ряде будет 101 (третье значение в скобках)
print(x)

y = np.sin(x)
print(y)


# Отрисовка графика командой plot(), в которую переданы массивы точек для x и y
# С помощью .show() выводится график
plt.plot(x, y)
plt.title('y=sin(x)')  #подписываем график сверху
plt.xlabel("Переменная X")  #подпись оси Х
plt.ylabel("Переменная Y")  #подпись оси Y

plt.show()




