import platform
import socket
import time
import obd
import datetime
import sys
import csv

DELAY = 2  # secs
archivo = 'datosAuto.csv'
miarchivo = open(archivo,'a')
writer = csv.writer(miarchivo,delimiter=',')
listacomandos =  list()
listaresultados = []
############
# armo arreglo con comandos soportados
# a partir del archivo
with open('comandosSoportadosAuto.csv') as csvfile:
  reader1 = csv.reader(csvfile)
  for row1 in reader1:
	row1 = row1[1].strip()
	coma = 'obd.commands.'+row1
	listacomandos.append(eval(coma))
#en listarcomandos tengo la lista de comandos soportados
############

def ejecutarComandos():
	timestamp = int(time.time())
	hora = datetime.datetime.now()
	misdatos = [hora,timestamp]
	for comand in listacomandos:
		cmd = comand
        	response = connection.query(cmd)
        	campo = response.value
		misdatos.extend([campo])
	writer.writerow(misdatos)
		
if __name__ == '__main__':
     connection = obd.OBD("/dev/ttyUSB0")
     try:
         with miarchivo:   
           while True:
            salida = ejecutarComandos()
            time.sleep(DELAY)
     except KeyboardInterrupt:
         miarchivo.close()
         sys.exit(0)
     miarchivo.close()
     sys.exit(1)
