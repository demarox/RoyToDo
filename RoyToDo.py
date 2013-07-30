#! /usr/bin/python
#unicode utf-8
# -*- coding: utf-8 -*-
from default_declarations import *
from f_roytodo import *
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
				print linea_de_division
				print borrow_admin() + leer()
				destroy_index = raw_input("indexe el elemento quiere borrar\n \a")
				if destroy_index.find("todo") != -1:
					destroy_all_eleccion = raw_input("esta seguro de querer borrar todo?")
					if destroy_all_eleccion == "si":
						destroy_all()
						continue
					else:
						pass	
				else:
					print "Procesando..."
					destroy(destroy_index)	
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
