class Ciudadano:
    def __init__(self, nombre, cedula, edad):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre} - Cédula: {self.cedula} - Edad: {self.edad}")


class Medico(Ciudadano):
    def __init__(self, nombre, cedula, edad, especialidad, consulta):
        super().__init__(nombre, cedula, edad)
        self.especialidad = especialidad
        self.consulta = consulta

    def realizar_consulta(self):
        print("Realizando consulta médica...")
        # Lógica específica para la consulta

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Especialidad: {self.especialidad} - Consulta: {self.consulta}")


class Abogado(Ciudadano):
    def __init__(self, nombre, cedula, edad, especialidad, despacho):
        super().__init__(nombre, cedula, edad)
        self.especialidad = especialidad
        self.despacho = despacho

    def resolver_caso(self):
        print("Resolviendo caso legal...")
        # Lógica específica para resolver casos

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Especialidad: {self.especialidad} - Despacho: {self.despacho}")


class Ingeniero(Ciudadano):
    def __init__(self, nombre, cedula, edad, especialidad, empresa):
        super().__init__(nombre, cedula, edad)
        self.especialidad = especialidad
        self.empresa = empresa

    def realizar_proyecto(self):
        print("Realizando proyecto de ingeniería...")
        # Lógica específica para proyectos de ingeniería

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Especialidad: {self.especialidad} - Empresa: {self.empresa}")


if __name__ == "__main__":
    ciudadano1 = Medico("Juan", "1234567890", 35, "Cardiología", "Hospital General")
    ciudadano1.mostrar_informacion()
    ciudadano1.realizar_consulta()

    ciudadano2 = Abogado("María", "987654321", 40, "Derecho Penal", "Bufete Legal")
    ciudadano2.mostrar_informacion()
    ciudadano2.resolver_caso()

    ciudadano3 = Ingeniero("Pedro", "5678901234", 30, "Ingeniería Civil", "Constructora ABC")
    ciudadano3.mostrar_informacion()
    ciudadano3.realizar_proyecto()
