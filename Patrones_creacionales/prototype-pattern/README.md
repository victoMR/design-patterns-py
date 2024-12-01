# Ejemplo del Patrón Prototipo

Este ejemplo demuestra el Patrón Prototipo utilizando una clase `Naruto`. El Patrón Prototipo es un patrón de diseño creacional que permite clonar objetos, incluso los complejos, sin acoplarse a sus clases específicas.

## Explicación del Código

La clase `Naruto` tiene dos atributos: `nombre` y `nivel_chakra`. Incluye un método `clonar` que utiliza `copy.deepcopy` de Python para crear una copia profunda del objeto. Esto asegura que todos los atributos del objeto sean copiados y que el clon sea independiente del original.

## Resultados 
Al ejecutar el código, obtendrás la siguiente salida
  
  ```bash
  Original:  Naruto(nombre=Naruto Uzumaki, nivel_chakra=100) - Dir de memoria:  2086203599440

Creando clones 5 de sombra:
Clone 1: Naruto(nombre=Naruto Uzumaki, nivel_chakra=75) - Dir de memoria: 2086203796768
Clone 2: Naruto(nombre=Naruto Uzumaki, nivel_chakra=75) - Dir de memoria: 2086203796864
Clone 3: Naruto(nombre=Naruto Uzumaki, nivel_chakra=75) - Dir de memoria: 2086203796960
Clone 4: Naruto(nombre=Naruto Uzumaki, nivel_chakra=75) - Dir de memoria: 2086203797056
Clone 5: Naruto(nombre=Naruto Uzumaki, nivel_chakra=75) - Dir de memoria: 2086203797152
  ```
## Explicación de los Resultados

* El objeto original Naruto tiene un nivel_chakra de 100.
* Se crean cinco clones utilizando el método clonar.
* El nivel_chakra de cada clon se reduce en 25, resultando en un nivel_chakra de 75 para cada clon.
* Las direcciones de memoria de los clones son diferentes de la del original y entre sí, lo que indica que son objetos separados.