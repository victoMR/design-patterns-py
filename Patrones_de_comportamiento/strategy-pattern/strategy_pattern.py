from abc import ABC, abstractmethod

# Estrategia abstracta
class MedioTransporte(ABC):
    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def calcular_beneficios(self):
        pass

    @abstractmethod
    def calcular_kilometros(self):
        pass

    @abstractmethod
    def calcular_contras(self):
        pass

    @abstractmethod
    def calcular_comodidad(self):
        pass

# Estrategia concreta: Avión
class Avion(MedioTransporte):
    def calcular_costo(self):
        return 1500  # Costo en dólares

    def calcular_beneficios(self):
        return "Rápido y seguro"

    def calcular_kilometros(self):
        return 11000  # Kilómetros de México a Japón

    def calcular_contras(self):
        return "Costoso y restricciones de equipaje"

    def calcular_comodidad(self):
        return "Alta"

# Estrategia concreta: Barco
class Barco(MedioTransporte):
    def calcular_costo(self):
        return 800  # Costo en dólares

    def calcular_beneficios(self):
        return "Experiencia única y vistas panorámicas"

    def calcular_kilometros(self):
        return 20000  # Kilómetros de México a Japón

    def calcular_contras(self):
        return "Lento y puede causar mareos"

    def calcular_comodidad(self):
        return "Media"

# Estrategia concreta: Tren
class Tren(MedioTransporte):
    def calcular_costo(self):
        return 1000  # Costo en dólares

    def calcular_beneficios(self):
        return "Cómodo y vistas del paisaje"

    def calcular_kilometros(self):
        return 15000  # Kilómetros de México a Japón

    def calcular_contras(self):
        return "No hay rutas directas y puede ser lento"

    def calcular_comodidad(self):
        return "Alta"

class Caminar(MedioTransporte):
    def calcular_costo(self):
        return 0  # Costo en dólares

    def calcular_beneficios(self):
        return "Ecológico y saludable"

    def calcular_kilometros(self):
        return 20000  # Kilómetros de México a Japón

    def calcular_contras(self):
        return "Lento y cansado"

    def calcular_comodidad(self):
        return "Baja"

# Contexto
class Viaje:
    def __init__(self, medio_transporte: MedioTransporte):
        self.medio_transporte = medio_transporte

    def mostrar_detalles(self):
        print(f"Costo: {self.medio_transporte.calcular_costo()} dólares")
        print(f"Beneficios: {self.medio_transporte.calcular_beneficios()}")
        print(f"Kilómetros: {self.medio_transporte.calcular_kilometros()} km")
        print(f"Contras: {self.medio_transporte.calcular_contras()}")
        print(f"Comodidad: {self.medio_transporte.calcular_comodidad()}")

# Uso del patrón Strategy
if __name__ == "__main__":
    print("Calcualndo detalles de los viajes de México a Japón: \n")
    viaje_avion = Viaje(Avion())
    print("Detalles del viaje en avión:")
    viaje_avion.mostrar_detalles()

    print("\nDetalles del viaje en barco:")
    viaje_barco = Viaje(Barco())
    viaje_barco.mostrar_detalles()

    print("\nDetalles del viaje en tren:")
    viaje_tren = Viaje(Tren())
    viaje_tren.mostrar_detalles()
    
    print("\nDetalles del viaje caminando:")
    viaje_caminando = Viaje(Caminar())
    viaje_caminando.mostrar_detalles()
    print("Estas loco por cierto si desea intentar eso\n")