from ManejadorViajeroFrecuente import ManejadorViajeroFrecuente

def test(manager):
	numViaj = input("Ingrese el numero de viajero. Para salir, ingrese LISTO\n")
	while numViaj.strip().upper() != "LISTO":
		dni = input("Ingrese el dni \n")
		nombre = input("Ahora el nombre \n")
		apelli = input("Ahora el apellido \n")
		cantMilla = input("Por ultimo, la cantidad de millas \n")
		
		manager.agregarViajero(numViaj, dni, nombre, apelli, cantMilla)
		
		numViaj = input("Ingrese el numero de viajero. Para salir, ingrese LISTO\n")

if __name__ == '__main__':
    manager = ManejadorViajeroFrecuente()
    test(manager)
    manager.cargarViajeroCsv("Viajeros")
    seguir = True
    while seguir:
     	print("A = Cargar Viajero")
		print("B = Gestionar Viajero")
     	print("Z = Cerrar Programa")
     	opci = input("\n").strip().upper()
     	
     	seguir = opci != 'Z'
     	
     	if seguir: 
     		if opci == 'A':
     			test(manager)
     		elif opci == 'B':
     			numViaj = input("Ingrese el numero de viajero\n")
     			manager.operacionesDeViajero(numViaj)
     		else:
     			print("Error. La opcion ingresada no es valida")
		
		print("Apellido, nombre y numero de viajero con mas millas")
		manager.listarInfoMaxMillas()
	
