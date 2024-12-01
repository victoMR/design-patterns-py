# Builder Pattern Example

Este proyecto demuestra el uso del patrón de diseño Builder en Python. El patrón Builder se utiliza para construir un objeto complejo paso a paso. Permite crear diferentes tipos y representaciones de un objeto utilizando el mismo código de construcción.

## Estructura del Proyecto

- `Telefono`: Clase que representa el producto final que se va a construir.
- `TelefonoBuilder`: Clase que proporciona métodos para configurar las diferentes partes del `Telefono`.
- `Director`: Clase que gestiona el proceso de construcción utilizando un `TelefonoBuilder`.
- Código del cliente: Código que utiliza el `Director` y el `TelefonoBuilder` para construir diferentes tipos de teléfonos.

## Clases

### Telefono

```python
class Telefono:
    def __init__(self):
        self.pantalla = None
        self.bateria = None
        self.camara = None
        self.procesador = None

    def __str__(self):
        return f"Teléfono [Pantalla: {self.pantalla}, Batería: {self.bateria}, Cámara: {self.camara}, Procesador: {self.procesador}]"
```

### TelefonoBuilder

```python
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
```

### Director

```python
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
```

## Salida

```bash
Teléfono [Pantalla: OLED 6.5 pulgadas, Batería: 4000mAh, Cámara: 108MP, Procesador: Snapdragon 888]
Teléfono [Pantalla: LCD 6.0 pulgadas, Batería: 3500mAh, Cámara: 48MP, Procesador: Snapdragon 720G]
Teléfono [Pantalla: LCD 5.5 pulgadas, Batería: 3000mAh, Cámara: 12MP, Procesador: Snapdragon 460]
```

## Conclusión

El patrón Builder es útil cuando se necesita construir un objeto complejo paso a paso. Permite crear diferentes tipos y representaciones de un objeto utilizando el mismo código de construcción. En este ejemplo, el `Director` utiliza un `TelefonoBuilder` para construir diferentes tipos de teléfonos con diferentes especificaciones.
