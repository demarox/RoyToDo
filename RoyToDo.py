#! /usr/bin/python
#unicode utf-8
# -*- coding: utf-8 -*-
import random
import time
from time import localtime, strftime
eleccion,trato_especial,deber,lista,res,continuar0,destroy_all_eleccion = "si", False, "", [],[],"si",""
quotes={1:"Otra cosa?\n", 2:"Algo mas?\n", 3:"Nada mas?\n", 4:"Le falto escribir algo?\n", 5:"Falto algo?\n", 6:"Que mas?\n"}
def crear(lista):
	archivo = open('royDatos.txt', 'a')
	for deberes in lista:
		archivo.write(deberes + "\n")
	archivo.close()
	#queremrlos darle buenas al usuario
def tiempo():
	m= strftime("%H:%M",localtime())
	t= int(strftime("%H",localtime()))
	if t >=7 and t<=14:
		return "Buenos dias, son las "+ m
	elif t >14 and t<=20:
		return "Buenas tardes, son las " + m
	else:
		return "Buenas noches, son las "+ m		
def random_quotes():
	extract =random.randint(1,6)
	return quotes[extract]
def leer():
	reuse,res = [],[]
	archivo= open('royDatos.txt','r')
	linea=archivo.readline()
	while linea  != "" :
		linea = linea.strip()
		print linea
		res.append(linea)
		linea=archivo.readline()
	archivo.close()
	print "------------------------------------"
	reuse = ", ".join(res)
	reuse = reuse.replace("\n","")
	reuse = reuse.lstrip()
	if not reuse:
		return " no tiene que hacer nada"
	else :
		return " tiene que " + reuse
def destroy(num):
	lista=[]
	archivo = open('royDatos.txt', 'r')	
	linea = archivo.readline()
	while linea  != "" :
		lista.append(linea)
		linea=archivo.readline()
	archivo.close()
	del lista[int(num)]
	archivo = open('royDatos.txt', 'w')
	for deberes in lista:
		archivo.write(deberes + "\n")
	archivo.close()
	time.sleep(3)
def	destroy_all():
	archivo = open("royDatos.txt", 'w')
	archivo.write("")
	archivo.close
	print "Eliminando todo"
	time.sleep(2)
	print "Eliminacion exitosa"
def admin_save(user):
	archivo= open('admin.txt', 'w')
	archivo.write(str(user))
	archivo.close
def borrow_admin():
	archivo = open('admin.txt', 'r')
	line = archivo.readline()
	archivo.close
	return str(line)	
#aqui empieza el programa
print """                     Hola usuario de Roy
 	xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                       Como te llamas ?
         """
while True:
	nombre = raw_input("Mi nombre es: ")
	if nombre.isdigit():
		print "No juegues conmigo. \n"
		continue

	elif nombre == borrow_admin() :
		trato_especial = True
		break
	else:
		break
print tiempo()
print "Espero que la pase bien"
while eleccion == "si":	
	lista=[]
	deber = raw_input("Que tienes que hacer?\n")
	if deber.find("ver") != -1 and trato_especial:
		print borrow_admin() + leer()
	elif deber.find("cambiar admin")!= -1 and trato_especial:
		admin_match = raw_input("Nombre del admin actual: \n")
		if admin_match == borrow_admin() :
			new_admin = raw_input("Nombre del admin nuevo: \n")
			admin_save(new_admin)
			print borrow_admin() + " es el nuevo admin"
		else:
			print "Incorrecto"	 
	elif deber.find("borrar") != -1	 and trato_especial:
		continuar0 = "si"
		while continuar0 == "si":
			if leer() == " no tiene que hacer nada":
				print "No hay nada que borrar "
				continuar0= "no"
				continue
			else:	
				print borrow_admin() + leer()
				destroy_index = raw_input("indexe el elemento quiere borrar\n \a")
				if destroy_index.isdigit():
					print "Procesando..."
					destroy(destroy_index)
				elif destroy_index.find("todo") != -1:
					destroy_all_eleccion = raw_input("esta seguro de querer borrar todo?")
					if destroy_all_eleccion == "si":
						destroy_all()
						continue
					else:
						pass	
				else:
					print "Ese no es un numero"	
				continuar0 = raw_input("Desea seguir borrando?\n ")		
	else:	
		while deber.find("no") and deber.find("nada") :
			lista.append(deber)
			deber = raw_input(random_quotes())
			deber = deber.lower()
		if trato_especial :
			print borrow_admin() +", sus datos seran anotados de inmediato."
			# parece que no lo lee
			crear(lista)
		else:
			print "hmmm pues haga algo de inmediato mi amigo procastinador :D"
	eleccion = raw_input("desea volver a usar la app? \n")
raw_input()