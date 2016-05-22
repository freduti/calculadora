# identacion

if 1 != 2 :
	print 'uno no es igual a dos :l'


# int = integer
# str = string

# aqui inicia nuestra calculadora
print 'Bienvenido a nuestra calculadora OP'

# le damos opciones al usuario
print '1) sumar'
print '2) restar'
print '3) multiplicar'
print '4) dividir'
print "5) salir"

# leemos lo que el usuario ha escrito :)
# nota: opcion aqui es una cadena de texto
opcion = raw_input('opcion >> ')

# y aqui es un numero entero :D
opcion = int(opcion)

if opcion > 5 or opcion < 1 :
	print 'esa opcion no es valida :l'
else:
	# aqui opcion ya no es un string
	if opcion == 1:
		# sumar +
		print 'vamos a sumar!!\n'
		numero1 = int(raw_input('primer numero >>'))
		numero2 = int(raw_input('segundo numero >>'))
		print numero1 + numero2
	if opcion == 2:
		# restar -
		print "Vamos a Restar!!\n"
		numero1 = int(raw_input('primer numero >>'))
		numero2 = int(raw_input('segundo numero >>'))
		print numero1 - numero2
	if opcion == 3:
		# multiplicar *
		print "vamos a Multiplicar!!\n"
		numero1 = int(raw_input('primer numero >>'))
		numero2 = int(raw_input('segundo numero >>'))
		print numero1 * numero2
	if opcion == 4:
		#dividir /
		print "Vamos a dividir!!\n"
		numero1 = int(raw_input('primer numero >>'))
		numero2 = int(raw_input('segundo numero >>'))
		print numero1 / numero2
	if opcion == 5:
		print "Adios!"
