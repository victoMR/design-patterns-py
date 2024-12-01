# Ejemplo de Strategy Pattern en Python

Este proyecto demuestra el uso del patrón de diseño Strategy en Python, utilizando como ejemplo diferentes medios de transporte para un viaje de México a Japón.

## Descripción

El patrón Strategy permite definir una familia de algoritmos, encapsular cada uno de ellos y hacerlos intercambiables. Este patrón permite que el algoritmo varíe independientemente de los clientes que lo utilizan.

En este ejemplo, hemos definido una clase abstracta `MedioTransporte` que declara métodos para calcular el costo, beneficios, kilómetros, contras y comodidad de un viaje. Luego, hemos creado clases concretas (`Avion`, `Barco`, `Tren`, `Caminando`) que implementan estos métodos de diferentes maneras.

La clase `Viaje` actúa como el contexto que utiliza una instancia de `MedioTransporte` para mostrar los detalles del viaje.

## Estructura del Proyecto

- `strategy_pattern.py`: Contiene la implementación del patrón Strategy con las clases `MedioTransporte`, `Avion`, `Barco`, `Tren` , `Viaje` y `Caminando`.


## Resultado Esperado

El programa imprime los detalles de un viaje de México a Japón utilizando diferentes medios de transporte.

```bash
Calcualndo detalles de los viajes de México a Japón: 

Detalles del viaje en avión:
Costo: 1500 dólares
Beneficios: Rápido y seguro
Kilómetros: 11000 km
Contras: Costoso y restricciones de equipaje
Comodidad: Alta

Detalles del viaje en barco:
Costo: 800 dólares
Beneficios: Experiencia única y vistas panorámicas
Kilómetros: 20000 km
Contras: Lento y puede causar mareos
Comodidad: Media

Detalles del viaje en tren:
Costo: 1000 dólares
Beneficios: Cómodo y vistas del paisaje
Kilómetros: 15000 km
Contras: No hay rutas directas y puede ser lento
Comodidad: Alta

Detalles del viaje caminando:
Costo: 0 dólares
Beneficios: Ecológico y saludable
Kilómetros: 20000 km
Contras: Lento y cansado
Comodidad: Baja
Estas loco por cierto si desea intentar eso
```

