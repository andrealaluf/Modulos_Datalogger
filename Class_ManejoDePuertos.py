# -*- coding: utf-8 -*-
##clase manejo de puertos que es utilizada para grabar en unidades usb los archivos
##agragar despues en el so que cuando detecte una conexion usb llame a esta clase

import os,os.path,shutil,time,datetime

class ManejoDePuertos:
	global archivosACopiar									#variable usada para poder comprobar si los archicos copiados son correctos
	global result											#variable usadapara poder comprobar los directorios
		 

	def CantidadDeArchivos(self):							#metodo que verifica la cantidad de archivos que hay para copiar
		DIR = '/home/andrea/Escritorio/pruebausb'			#directorio de donde se copian los archivos
		print len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
		self.archivosACopiar=len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]) #cantidad de archivos en el directorio
	
	def EspacioDisponibleEnUnidadExt(self):					#metodo que comprueba si hay espacio libre en la unidad usb
		sisf = os.statvfs('/media/andrea/F735-3177')		
		print "%s megas libres" % (sisf.f_bavail * sisf.f_bsize / 1048576)		#espacio libre en disco

	def CopiaLogsEnUnidadExt(self):							#metodo que guarda los archivos a copiar
		ts = time.time()
		dia=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')	#fecha y hora a concatenar con el nombre de archivo
		src='/home/andrea/Escritorio/pruebausb'				#directorio
		dst='/media/andrea/F735-3177/logs'					#unidad conectadaa
		result1 = os.path.join(dst, dia)					#guardo en resul1 el nombre del archivo mas la inclusion del dia
		self.result=result1									#guardo en result lo que tengo en result1 asi lo puedo usar en el metodo ComprovacionDArchivos
		#print result1
		shutil.copytree(src,result1)						#copia todos los archivos en la direccion especificada
		if os.path.exists(result1): 
			print "El fichero existe" 
		else: 
			print "El fichero no existe"
			
	def ComprobacionDArchivos(self):						#metodo que comprueba la cantidad de rchivos copiados
		DIR2=self.result									#direccion de comprobacion
		#print self.result
		archivosCopiados=len([name for name in os.listdir(DIR2) if os.path.isfile(os.path.join(DIR2, name))])	#medice la cantidad de archivos copiados
		if(archivosCopiados==self.archivosACopiar):			#comparacion entre los archivos copiados en la unidad exraibles y los guardados en el datalogger
			print 'todos los archivos se copiaron'
		else:
			print 'se perdieron archivos'
		
def main():
	x=ManejoDePuertos()
	x.CantidadDeArchivos()
	x.EspacioDisponibleEnUnidadExt()
	x.CopiaLogsEnUnidadExt()
	x.ComprobacionDArchivos()
	
if __name__=="__main__":
	main()
