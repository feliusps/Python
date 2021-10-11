import random
indice=0
while indice==0:
	tirar  = int(input("Escribe 1 si quieres tirar y 0 si no qieres tirar: "))
	if tirar==1:
		dado1=random.randint(1,6)
		dado2=random.randint(1,6)
		print("Primer dado:",dado1)
		print("Segundo dado:",dado2)
		suma=dado1+dado2
		print("la suma es: ")
		print(suma)
	elif tirar==0:
		print("Programa terminado")
		break
	else:
		print("Opcion no valida")
		break