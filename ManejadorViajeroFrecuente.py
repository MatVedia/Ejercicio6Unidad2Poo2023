from ClaseViajeroFrecuente import ViajeroFrecuente
import csv

class ManejadorViajeroFrecuente():
    def __init__(self):
        self.__listaViajeros = []
    
    def __buscarViajero(self, numBuscado):
        i = 0
        N = len(self.__listaViajeros)
        viajero = None
        while i < N and self.__listaViajeros[i].getNumeroViajero() != numBuscado:
            i += 1
        if i < N:
            viajero = self.__listaViajeros[i]
        return viajero
    
    def __leerOpcionDeUsuario(self):
        print("A = Consultar Cantidad de millas.")
        print("B = Acumular Millas.")
        print("C = Canjear Millas.")
        print("Z = Cerrar Sesion.")
        return input("\nQue desea hacer? ").upper()
        
    
    def operacionesDeViajero(self, numeroDeViajero):
        numeroDeViajero = numeroDeViajero.strip()
        if not numeroDeViajero.isdigit():
            print("Error. Se espera que ingrese un numero")
        else:
            viajero = self.__buscarViajero(int(numeroDeViajero))
            if viajero == None:
                print('Error. El numero de viajero ingresado, {}, no existe.'.format(numeroDeViajero))
            else:
                opci = self.__leerOpcionDeUsuario()
                while opci != 'Z':
                    if opci == 'A':
                        print('Su cantidad actual de millas es {}'.format(viajero.getCanitidadTotalDeMillas()))
                    elif opci == 'B':
                        cantNuevasMillas = input("Ingrese la cantidad de millas a registrar\n").strip()
                        if not cantNuevasMillas.strip().isdigit():
                            print("Error. Debe ingresar un numero")
                        else:
                            viajero + int(cantNuevasMillas.strip())
                    elif opci == 'C':
                        cantidadACanjear = input("Ingrese la cantidad de millas que desea canjear\n").strip()
                        if not cantidadACanjear.isdigit():
                            print("Error. Se espera un numero.")
                        else:
                            actualizado = viajero + int(cantidadACanjear.strip())
                            print('Su cantidad actual de millas es {}'.format(actualizado.getCanitidadTotalDeMillas()))
                    else:
                        print("Error. No ingreso una opcion valida.")
                    opci = self.__leerOpcionDeUsuario()
                    
                    
    def agregarViajero(self, numViaj, dni, nombre, apellido, cantMillas):
    	if not numViaj.strip().isdigit():
    		print("Error. El numero de viajero ingresado no es valido.")
        elif not dni.replace('.', '').strip().isdigit():
    		print("Error. El dni ingresado no es valido.")
        elif not cantMillas.strip().isdigit() or int(cantMillas.strip()) < 0:
    		print("Error. La cantidad de millas ingresadas no es valida.")
    	elif self.__buscarViajero(numViaj.strip()) != None:
    		print ("El numero de viajero ingresado ya esta en uso")
    	else:
    		self.__listaViajeros.append(ViajeroFrecuente(int(numViaj.strip()), dni.replace(".", ""), nombre, apellido, int( cantMillas.strip())))
    
    def cargarViajeroCsv(self, nomArchi):
    	archi = open(nomArchi.replace('.csv', '') + '.csv', 'r')
    	lector = csv.reader(archi, delimiter = ',')
    	for viajero in lector:
    		self.agregarViajero(viajero[0], viajero[1], viajero[2], viajero[3],  viajero[4])
    	
    	archi.close()
    
    def listarInfoMaxMillas(self):
        max = self.__listaViajeros[0]
        N = len(self.__listaViajeros)
        for i in range(1, N):
             if self.__listaViajeros > max:
                  max = self.__listaViajeros[i]
        
        for viajero in self.__listaViajeros:
             if max.getCanitidadTotalDeMillas() == viajero.getCanitidadTotalDeMillas():
                  print("{} {Viajero Numero: }".format(viajero.getApellidoNombre(), viajero.getNumeroViajero))
    

 
 
 
