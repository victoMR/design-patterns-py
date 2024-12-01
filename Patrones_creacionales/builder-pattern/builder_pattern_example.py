
class Telefono:
    def __init__(self):
        self.pantalla = None
        self.bateria = None
        self.camara = None
        self.procesador = None

    def __str__(self):
        return f"Teléfono [Pantalla: {self.pantalla}, Batería: {self.bateria}, Cámara: {self.camara}, Procesador: {self.procesador}]"

class TelefonoBuilder:
    def __init__(self):
        self.telefono = Telefono()

    def set_pantalla(self, pantalla):
        self.telefono.pantalla = pantalla
        return self

    def set_bateria(self, bateria):
        self.telefono.bateria = bateria
        return self

    def set_camara(self, camara):
        self.telefono.camara = camara
        return self

    def set_procesador(self, procesador):
        self.telefono.procesador = procesador
        return self

    def build(self):
        return self.telefono

# Director para gestionar el proceso de construcción
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construir_telefono_gama_alta(self):
        self.builder.set_pantalla("OLED 6.5 pulgadas").set_bateria("4000mAh").set_camara("108MP").set_procesador("Snapdragon 888")
        return self.builder.build()

    def construir_telefono_gama_media(self):
        self.builder.set_pantalla("LCD 6.0 pulgadas").set_bateria("3500mAh").set_camara("48MP").set_procesador("Snapdragon 720G")
        return self.builder.build()

    def construir_telefono_gama_baja(self):
        self.builder.set_pantalla("LCD 5.5 pulgadas").set_bateria("3000mAh").set_camara("12MP").set_procesador("Snapdragon 460")
        return self.builder.build()

# Código del cliente para probar el patrón Builder
if __name__ == "__main__":
    builder = TelefonoBuilder()
    director = Director(builder)

    telefono_gama_alta = director.construir_telefono_gama_alta()
    print(telefono_gama_alta)

    telefono_gama_media = director.construir_telefono_gama_media()
    print(telefono_gama_media)

    telefono_gama_baja = director.construir_telefono_gama_baja()
    print(telefono_gama_baja)