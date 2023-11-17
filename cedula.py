class Ciudadano:
    def __init__(self, nombre, cedula, edad):
        self._nombre = nombre
        self._cedula = cedula
        self._edad = edad

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_cedula(self):
        return self._cedula

    def set_cedula(self, cedula):
        if len(cedula) >= 8 and len(cedula) <= 10:
            self._cedula = cedula
        else:
            print("es correcto el numero de documento")

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        if edad > 0:
            self._edad = edad
        else:
            print("La edad debe ser un número positivo mayor que cero")

    def mostrar(self):
        print(f"Nombre: {self._nombre} - Edad: {self._edad} - CC: {self._cedula}")

    def esMayorDeEdad(self):
        return self._edad >= 18


if __name__ == "__main__":
    ciudadano = Ciudadano("juan", "2345768913", 19)
    ciudadano.mostrar()  
    print(ciudadano.esMayorDeEdad())  

    ciudadano.set_edad(16) 
    ciudadano.set_cedula("01020304050607")  



