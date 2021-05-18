import numpy as np
from PIL import Image, ImageFilter, ImageGrab
from array import *
import time

array_width = int
array_width = ImageGrab.grab().size[0]

current_columns = np.zeros((5, array_width, 3))
previous_columns = np.zeros((5, array_width, 3))


while True :
	image = ImageGrab.grab()
	width = image.size[0] #Определяем ширину.
	height = image.size[1] #Определяем высоту.
	pix = image.load() #Выгружаем значения пикселей.
	summaPic=0
	summaBlack=0
	summaWhite=0
	summaDesktop=0
	summaGreenInformer=0
	summaBlueInformer=0
	interval = int
	interval=height//4
	i=0
	j = 0
	p = 0
	SovpadenieGreen = 0
	SovpadenieBlue = 0
	SovpadeniePlayer = 0
	SummaGreen = 0
	SummaBlue = 0
	SummaPlayer = 0
	massiv = np.zeros((5, 1))


	arr = np.asarray(image)
	
	current_columns[0] = arr[0]
	current_columns[1] = arr[interval]
	current_columns[2] = arr[2 * interval]
	current_columns[3] = arr[3 * interval]
	current_columns[4] = arr[height-1]


	for y in range(height):
			for x in range(width):
				r = pix[x, y][0]
				g = pix[x, y][1]
				b = pix[x, y][2]
	
				summaPic +=1
				result = [r], [g], [b]  # строка со значением пиксеоей
				if (0==r) and (0==g) and (0==b) : summaBlack+=1   #Количество совпадений черных пикселей
				if (r==255) and (g == 255) and (b==255) : summaWhite+=1 #Количество совпадений белых пикселей
				if (191<= r <= 201) and (218<= g <= 228) and (151<=b<= 161): summaDesktop += 1 #Количество совпадений  пикселей с изображением рабочего стола

	if (previous_columns[0][0][0] != 0):
		for i in range(len(previous_columns)):
			for j in range(len(previous_columns[i])):
				if ((previous_columns[i, j, 0] == current_columns[i, j, 0] and previous_columns[i, j, 0] == 20)
					and (previous_columns[i, j, 1] == current_columns[i, j, 1] and previous_columns[i, j, 1] == 162)
					and (previous_columns[i, j, 2] == current_columns[i, j, 2] and previous_columns[i, j, 2] == 0)):
					SovpadenieGreen += 1
				if ((previous_columns[i, j, 0] == current_columns[i, j, 0] and previous_columns[i, j, 0] == 0)
					and (previous_columns[i, j, 1] == current_columns[i, j, 1] and previous_columns[i, j, 1] == 103)
					and (previous_columns[i, j, 2] == current_columns[i, j, 2] and previous_columns[i, j, 2] == 179)):
					SovpadenieBlue += 1
				if ((previous_columns[i, j, 0] == current_columns[i, j, 0] and previous_columns[i, j, 0] == 196)
					and (previous_columns[i, j, 1] == current_columns[i, j, 1] and previous_columns[i, j, 1] == 223)
					and (previous_columns[i, j, 2] == current_columns[i, j, 2] and previous_columns[i, j, 2] == 156)):
				    SovpadeniePlayer += 1
			if SovpadenieGreen >= 200: massiv[i] = 10
			if SovpadenieBlue >= 200: massiv[i] = 20
			if   summaPic * 80 / 100 > summaDesktop :
				if SovpadeniePlayer  >= 200: massiv[i] = 30

	previous_columns = current_columns
	for p in range(len(massiv)):
		for o in range(len(massiv[p])):
			if (massiv[p, o] == 10): SummaGreen += 1
			if (massiv[p, o] == 20): SummaBlue += 1
			if (massiv[p, o] == 30): SummaPlayer += 1
	if SummaGreen >= 2: print("Ошибка, зеленый информер")
	if SummaBlue >= 2: print("Ошибка, синий информер")
	if SummaPlayer >= 2: print("Ошибка, плеер в окне")


#	print(result, + summaPic, + summaBlack, summaWhite, + summaDesktop, + summaBlueInformer, + summaGreenInformer)
	if summaPic * 80 / 100 <= summaBlack: print("Ошибка черного экрана")
	if summaPic * 80 / 100 <= summaWhite: print("Ошибка белого экрана")
	if summaPic * 80 / 100 <= summaDesktop: print("Ошибка, рабочий стол")

	time.sleep(60)

