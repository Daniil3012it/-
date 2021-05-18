import numpy as np
from PIL import Image, ImageFilter, ImageGrab
from array import *
import time

array_width = int
array_width = ImageGrab.grab().size[0]

current_columns = np.zeros((5, array_width, 3))
previous_columns = np.zeros((5, array_width, 3))

while True:
    #	image = Image.open('C:\\Users\Admin\\PycharmProjects\\screenshots\\1neok\\Desktop\\BKB-WOD-K15CC00-46.jpg')  #Открываем изображение.
    image = ImageGrab.grab()
    width = image.size[0]  # Определяем ширину.
    height = image.size[1]  # Определяем высоту.
    pix = image.load()  # Выгружаем значения пикселей.
    interval = int
    interval = height // 4
    i = 0
    j=0
    p=0
    SovpadenieGreen = 0
    SovpadenieBlue=0
    SovpadenieDesktop=0

    SummaGreen=0
    SummaBlue=0
    SummaDesktop=0
    arr = np.asarray(image)

    current_columns[0] = arr[0]
    current_columns[1] = arr[interval]
    current_columns[2] = arr[2 * interval]
    current_columns[3] = arr[3 * interval]
    current_columns[4] = arr[height - 1]
    massiv = np.zeros((5, 1))


    if (previous_columns[0][0][0] != 0):
        for i in range(len(previous_columns)):
            for j in range(len(previous_columns[i])):
              if  ((previous_columns[i, j, 0] == current_columns[i, j, 0] and previous_columns[i, j, 0] == 20)
                  and (previous_columns[i, j, 1] == current_columns[i, j, 1] and previous_columns[i, j, 1] == 162)
                  and (previous_columns[i, j, 2] == current_columns[i, j, 2] and previous_columns[i, j, 2] == 0)) :
                    SovpadenieGreen += 1
              if ((previous_columns[i, j, 0] == current_columns[i, j, 0] and previous_columns[i, j, 0] == 0)
                  and (previous_columns[i, j, 1] == current_columns[i, j, 1] and previous_columns[i, j, 1] == 103)
                  and (previous_columns[i, j, 2] == current_columns[i, j, 2] and previous_columns[i, j, 2] == 179)):
                    SovpadenieBlue += 1
              if ((previous_columns[i, j, 0] == current_columns[i, j, 0] and previous_columns[i, j, 0] == 196)
                      and (previous_columns[i, j, 1] == current_columns[i, j, 1] and previous_columns[i, j, 1] == 223)
                      and (previous_columns[i, j, 2] == current_columns[i, j, 2] and previous_columns[i, j, 2] == 156)):
                  SovpadenieDesktop += 1
            if SovpadenieGreen >= 200 : massiv[i]= 10
            if SovpadenieBlue >= 200 : massiv[i] = 20
            if SovpadenieDesktop >= 200 : massiv[i] = 30
    previous_columns = current_columns
    for p in range(len(massiv)) :
        for o in range(len(massiv[p])) :
            if (massiv[p, o] == 10) : SummaGreen += 1
            if (massiv[p, o] == 20) : SummaBlue += 1
            if (massiv[p, o] == 30): SummaDesktop +=1
    if SummaGreen >= 2 : print("Ошибка, зеленый информер")
    if SummaBlue >= 2 : print("Ошибка, синий информер")
    if SummaDesktop >= 2 : print("Ошибка, плеер в окне")
    time.sleep(3)