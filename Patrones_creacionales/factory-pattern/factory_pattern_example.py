from abc import ABC, abstractmethod

# Clase base abstracta para Computadoras
class Computadora(ABC):
    @abstractmethod
    def obtener_especificaciones(self):
        pass

# Clase concreta para Desktop
class Escritorio(Computadora):
    def obtener_especificaciones(self):
        return "Escritorio: 16GB RAM, 1TB HDD, Intel i7"

# Clase concreta para Laptop
class Portatil(Computadora):
    def obtener_especificaciones(self):
        return "Portátil: 8GB RAM, 512GB SSD, Intel i5"

# Clase concreta para Server
class Servidor(Computadora):
    def obtener_especificaciones(self):
        return "Servidor: 32GB RAM, 4TB SSD, AMD EPYC"

# Clase fábrica para crear computadoras
class FabricaComputadoras:
    @staticmethod
    def crear_computadora(tipo_computadora):
        if tipo_computadora == "escritorio":
            return Escritorio()
        elif tipo_computadora == "portatil":
            return Portatil()
        elif tipo_computadora == "servidor":
            return Servidor()
        else:
            raise ValueError(f"Tipo de computadora desconocido: {tipo_computadora}")

# Código del cliente para probar el patrón de fábrica
if __name__ == "__main__":
    # Crear un escritorio
    escritorio = FabricaComputadoras.crear_computadora("escritorio")
    print(escritorio.obtener_especificaciones())

    # Crear un portátil
    portatil = FabricaComputadoras.crear_computadora("portatil")
    print(portatil.obtener_especificaciones())

    # Crear un servidor
    servidor = FabricaComputadoras.crear_computadora("servidor")
    print(servidor.obtener_especificaciones())