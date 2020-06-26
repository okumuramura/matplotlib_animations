import matplotlib.pyplot as plt 
import random

count = 30 # Количество элементов в массиве

array = [random.randint(0,256) for _ in range(count)] # Создание массива заданного размера

fig = plt.figure(figsize=(18,8)) # Размер окна

for i in range(count):

    # Оформление графика
    plt.cla() # Отчищаем график
    plt.title("Select sort") # Заголовок
    plt.xticks(list(range(count))) # Метки снизу
    plt.yticks([]) # Метки слева (убираем)
    plt.imshow([array], cmap = "magma") # Вывод изображения (cmap - цветовое отображение)

    # Добавление значений ячеек
    for j in range(count):
        color = "#000000" if array[j] > 127 else "#ffffff" # Цвет шрифта в зависимости от значения ячейки
        plt.text(j, 0, array[j], color = color, weight = 1000, ha = "center", va = "center") # Вставка текста

    plt.pause(0.5) # Вывод на экран с задержкой 0.3 c
    
    # Сортировка (выбором):
    min_element = array[i]
    min_index = i
    for t in range(i, count):
        if array[t] < min_element:
            min_element = array[t]
            min_index = t
    array[i], array[min_index] = array[min_index], array[i]
    # print(*array, sep=" ")

plt.show()
# Проверка
# if array == sorted(array): print("OK!")
# else: print("No!")