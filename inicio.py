import commands

archivo = 'comandosSoportadosAuto.csv'
miarchivo = open(archivo,'w')
writer = csv.writer(miarchivo,delimiter=',')
a = []
b = []
salida = 1
def inicializaAuto():
	print("Obteniendo comandos soportados por el auto")
	lista = commands.getoutput('python listar_comandos.py > ComandosAuto.csv ')
	print("Conviertiendo datos..")
	with open('lista_completa_comandos.csv') as csvfile:
	 reader1 = csv.reader(csvfile,delimiter=',')
	 for row1 in reader1:
		b.append(row1)

	with open('ComandosAuto.csv') as csvfile:
	 reader = csv.reader(csvfile,delimiter=':')
	 for row in reader:
	   if row[0] < '02':
        	 sepa = row[0]
		 modo = sepa[0:2]
		 comando = sepa[2:4]
		 a.append(comando)

	with miarchivo:   
		for comand in b:
			if comand[0] in a:
				misdatos = [comand[0],comand[1],comand[2]]
				writer.writerow(misdatos)
	miarchivo.close()
###aca termina de convertir los csv, ahora estan listos para procesar en el scrip ppal

while salida != 3:
	print("Seleccione su opcion \
		1 - Configurar auto \
		2 - Inicializar auto \
		3 - Salir")
	opcion = input()
	if opcion == 1:
		print opcion
	elif opcion == 2:
		opc = inicializaAuto()
		print opcion
	elif opcion == 3:
		salida = 3
		print "chau"
	else:
		print "elija otra opcion"

