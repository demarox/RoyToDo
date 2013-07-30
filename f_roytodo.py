import random
import time
from time import localtime, strftime
from default_declarations import *
def crear(lista):
	archivo = open('royDatos.txt', 'a')
	for deberes in lista:
		archivo.write(deberes + "\n")
	archivo.close()
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
		res.append(linea)
		linea=archivo.readline()
	archivo.close()
	reuse = ", ".join(res)
	reuse = reuse.replace("\n","")
	reuse = reuse.lstrip()
	if not reuse:
		return " no tiene que hacer nada"
	else :
		return " tiene que " + reuse
def destroy(tin_can):
	lista=[]
	archivo = open('royDatos.txt', 'r')	
	linea = archivo.readline()
	while linea  != "" :
		lista.append(linea)
		linea=archivo.readline() 
	archivo.close()
#debugger:	print lista 
	if str(tin_can+"\n") in lista or tin_can.isdigit():
		if tin_can.isdigit():
			del lista[int(tin_can)]
		else:
			lista.remove(tin_can+"\n")

		lista_filtrada = [n for n in lista if n != "\n" or n != '\n']			
		archivo = open('royDatos.txt', 'w')
		for deberes in lista_filtrada:
			archivo.write(deberes + "\n")
		archivo.close()
		time.sleep(3)
	else:
		print "El dato que quizo borrar no existe."		
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
	