import numpy as np
import matplotlib.pyplot as plt

# 1
# Создайте три вектора, из пяти элементов каждый. Один вектор должен быть заполнен нулями, второй - единицами, а третий - цифрами 3.

null_vector = np.zeros(5, dtype=int)
one_vector = np.ones(5, dtype=int)
three_vector = np.full(5, 3)

print(null_vector)
print(one_vector)
print(three_vector)
