class Articulo:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def calcular_precio_bruto(self):
        return self._precio

    def calcular_iva(self):
        return 0

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        self._precio = precio


class Alimento(Articulo):
    def __init__(self, nombre, precio, iva):
        super().__init__(nombre, precio)
        self._iva = iva

    def calcular_precio_bruto(self):
        return self._precio

    def calcular_iva(self):
        return self._precio * self._iva

    def get_iva(self):
        return self._iva

    def set_iva(self, iva):
        self._iva = iva


def calcular_precio_total(articulos):
    precio_total = 0
    iva_total = 0

    for articulo in articulos:
        precio_total += articulo.calcular_precio_bruto()
        iva_total += articulo.calcular_iva()

    return precio_total, iva_total


if __name__ == "__main__":
    articulos = [
        Alimento("Manzanas", 10, 0.19),
        Alimento("Arroz", 5, 0.05),
        Alimento("Leche", 20, 0.0)
    ]

    articulos[0].set_precio(12)  # Modificar el precio de las manzanas
    articulos[1].set_nombre("Arroz Integral")  # Modificar el nombre del arroz

    precio_total, iva_total = calcular_precio_total(articulos)

    print(f"Precio total: {precio_total}")
    print(f"IVA total: {iva_total}")
