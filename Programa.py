# codigo en Python
i,sum=0,0
num=float(input('Ingrese el numero de estudiantes:'))
while(i<num):
	sum += float(input('Ingrese nota:'))
	i += 1
	if i==num:
		print(sum/i)
