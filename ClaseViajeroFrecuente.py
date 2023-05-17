class ViajeroFrecuente():
    def  __init__(self, numviaj, dni, nom, apelli, millas):
        self.__num_viajero = numviaj
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = apelli
        self.__millas_acum = millas

    def getApellidoNombre(self):
        return self.__apellido + ' ' + self.__nombre
    
    def getNumeroViajero(self):
        return self.__num_viajero
    
    def getCanitidadTotalDeMillas(self):
        return self.__millas_acum
    
    def __gt__(self, otro): 
        if type(self) == type(otro):
            return self.__millas_acum > otro.__millasAcum
    
    def __add__(self, nuevasMillas): #Acumular millas
        if type(nuevasMillas) == int:
            if nuevasMillas >= 0:
                self.__millas_acum += nuevasMillas
        return self
    
    def __sub__(self, cantACanjear): #Canjear Millas
        if type(cantACanjear) == int:
            if cantACanjear >= 0 and cantACanjear <= self.__millas_acum:
                self.__millas_acum -= cantACanjear
        return self