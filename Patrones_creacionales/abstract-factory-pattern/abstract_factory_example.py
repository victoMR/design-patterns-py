from abc import ABC, abstractmethod

# Productos Abstractos
class Hoja(ABC):
    @abstractmethod
    def get_tipo(self):
        pass

class HojaA4(Hoja):
    def get_tipo(self):
        return "Hoja A4"

class HojaCarta(Hoja):
    def get_tipo(self):
        return "Hoja Carta"

# Fábrica Abstracta
class FabricaHojas(ABC):
    @abstractmethod
    def crear_hoja(self):
        pass

class FabricaHojasA4(FabricaHojas):
    def crear_hoja(self):
        return HojaA4()

class FabricaHojasCarta(FabricaHojas):
    def crear_hoja(self):
        return HojaCarta()

# Código del Cliente
def imprimir_tipo_hoja(fabrica):
    hoja = fabrica.crear_hoja()
    print(f"Tipo de hoja creada: {hoja.get_tipo()}")

if __name__ == "__main__":
    fabrica_a4 = FabricaHojasA4()
    fabrica_carta = FabricaHojasCarta()

    imprimir_tipo_hoja(fabrica_a4)
    imprimir_tipo_hoja(fabrica_carta)