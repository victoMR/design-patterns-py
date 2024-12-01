# Patrón de Diseño Factory

Este proyecto demuestra el uso del patrón de diseño Factory en Python para la creación de diferentes tipos de computadoras. El patrón Factory es un patrón creacional que proporciona una interfaz para crear objetos en una superclase, pero permite a las subclases alterar el tipo de objetos que se crearán.

## Estructura del Código

### Clases Abstractas y Concretas

1. **Computadora (Clase Abstracta)**: Define una interfaz común para todas las computadoras.
    ```python
    from abc import ABC, abstractmethod

    class Computadora(ABC):
        @abstractmethod
        def obtener_especificaciones(self):
            pass
    ```

2. **Escritorio, Portatil, Servidor (Clases Concretas)**: Implementan la interfaz definida por la clase abstracta `Computadora`.
    ```python
    class Escritorio(Computadora):
        def obtener_especificaciones(self):
            return "Escritorio: 16GB RAM, 1TB HDD, Intel i7"

    class Portatil(Computadora):
        def obtener_especificaciones(self):
            return "Portátil: 8GB RAM, 512GB SSD, Intel i5"

    class Servidor(Computadora):
        def obtener_especificaciones(self):
            return "Servidor: 32GB RAM, 4TB SSD, AMD EPYC"
    ```

### Clase Fábrica

La clase `FabricaComputadoras` es responsable de crear instancias de las diferentes computadoras basándose en el tipo solicitado.
```python
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
```

## Uso del Patrón Factory

1. Crear una instancia de la clase `FabricaComputadoras`.
    ```python
    fabrica = FabricaComputadoras()
    ```

2. Crear diferentes tipos de computadoras utilizando el método `crear_computadora`.
    ```python
    escritorio = fabrica.crear_computadora("escritorio")
    portatil = fabrica.crear_computadora("portatil")
    servidor = fabrica.crear_computadora("servidor")
    ```

3. Obtener las especificaciones de cada tipo de computadora.
    ```python
    print(escritorio.obtener_especificaciones()) # Escritorio: 16GB RAM, 1TB HDD, Intel i7
    print(portatil.obtener_especificaciones()) # Portátil: 8GB RAM, 512GB SSD, Intel i5
    print(servidor.obtener_especificaciones()) # Servidor: 32GB RAM, 4TB SSD, AMD EPYC
    ```
## Salida del Programa

La salida del programa muestra las especificaciones de cada tipo de computadora creada.
```
Escritorio: 16GB RAM, 1TB HDD, Intel i7
Portátil: 8GB RAM, 512GB SSD, Intel i5
Servidor: 32GB RAM, 4TB SSD, AMD EPYC
```

## Conclusión

El patrón de diseño Factory es útil cuando se necesita crear diferentes tipos de objetos que comparten una interfaz común. En lugar de instanciar directamente las clases concretas, se delega la creación de objetos a una clase fábrica que decide qué tipo de objeto crear en función de los parámetros proporcionados.
