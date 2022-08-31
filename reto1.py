#ENTRADAS=VARIABLES=REFERENCIA EN MEMORIA
nivelAgua=int(input("Digite el nivel de agua: "))

#PROCESOS
if (nivelAgua >=0 and nivelAgua<20):
    #Sin agua
    print(f'El nivel de agua es {nivelAgua} y este es bajo')
elif (nivelAgua>=20 and nivelAgua<400):
    #Nivel ok
    print(f'El nivel de agua es {nivelAgua} y este es normal')
elif (nivelAgua>=400):
    #Alerta nivel crítico
    print(f'El nivel de agua es {nivelAgua} y este es alto y crítico')
else:
    print(f'El nivel de agua no es valido')

#SALIDAS