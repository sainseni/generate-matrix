import random
import numpy as np

#Membuat angka sebarang
def randoms():
	return random.randint(0,99)

#konversi array ke tupple
def convert(array):
	tupple = tuple(array)
	return tupple
#Memasukan angka random ke array
def genNum(long):
	array = []
	for i in range(0,long):
		array.append(randoms())
	return array
#Membuat matrix sebaris
def vmatrix(long):
	array = genNum(long)
	return np.array(array)
#Membuat matrix dimensional
def dmatrix(a,b):
	array = []
	for i in range(0,a):
		for j in range(1,b):
			t = convert(vmatrix(b))
		array.append(t)
	array = np.array(array)
	return array

a = int(input(' Vertical : '))
b = int(input(' Horizontal : '))
v = dmatrix(a,b)
print(v)