# Ejemplo del Patrón Abstract Factory

Este proyecto demuestra el uso del patrón de diseño Abstract Factory en Python. El patrón Abstract Factory proporciona una interfaz para crear familias de objetos relacionados o dependientes sin especificar sus clases concretas.

## Estructura del Proyecto

- `Hoja`: Clase abstracta que representa el producto.
- `HojaA4` y `HojaCarta`: Clases concretas que implementan `Hoja`.
- `FabricaHojas`: Clase abstracta que define el método para crear hojas.
- `FabricaHojasA4` y `FabricaHojasCarta`: Clases concretas que implementan `FabricaHojas`.
- Código del cliente: Código que utiliza las fábricas para crear hojas y mostrar su tipo.

## Clases

### Hoja

```python
from abc import ABC, abstractmethod

class Hoja(ABC):
    @abstractmethod
    def get_tipo(self):
        pass
```

## HojaA4 y HojaCarta
  
  ```python
  class HojaA4(Hoja):
    def get_tipo(self):
        return "Hoja A4"

class HojaCarta(Hoja):
    def get_tipo(self):
        return "Hoja Carta"
  ```

## FabricaHojas

```python
class FabricaHojas(ABC):
    @abstractmethod
    def crear_hoja(self):
        pass
```

## FabricaHojasA4 y FabricaHojasCarta

```python

class FabricaHojasA4(FabricaHojas):
    def crear_hoja(self):
        return HojaA4()

class FabricaHojasCarta(FabricaHojas):
    def crear_hoja(self):
        return HojaCarta()
```

## Salida del Programa

```bash
Tipo de hoja creada: Hoja A4
Tipo de hoja creada: Hoja Carta
```

## Conclusión

El patrón Abstract Factory es útil cuando se necesita crear familias de objetos relacionados o dependientes sin especificar sus clases concretas. En este ejemplo, `FabricaHojas` es la interfaz que define el método para crear hojas, y `FabricaHojasA4` y `FabricaHojasCarta` son las implementaciones concretas que crean hojas de tipo `HojaA4` y `HojaCarta`, respectivamente. El código del cliente utiliza las fábricas para crear hojas y mostrar su tipo.
