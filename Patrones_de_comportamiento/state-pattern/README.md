# Simulación de Git con el Patrón State

Este proyecto demuestra el uso del patrón de diseño State para simular los estados de un repositorio Git. Los estados incluyen sin cambios, agregando cambios, cambios en stage y cambios commiteados.

## Clases

### Estado
Una clase base abstracta que define el método `manejar`, el cual debe ser implementado por todas las clases de estado concretas.

### EstadoSinCambios
Representa el estado donde no hay cambios en el repositorio. Transiciona a `EstadoAgregarCambios`.

### EstadoAgregarCambios
Representa el estado donde se están agregando cambios al repositorio. Transiciona a `EstadoStaged`.

### EstadoStaged
Representa el estado donde los cambios están en el área de stage. Transiciona a `EstadoCommit`.

### EstadoCommit
Representa el estado donde los cambios han sido commiteados. Transiciona de vuelta a `EstadoSinCambios`.

### Contexto
Mantiene una instancia de una subclase de `Estado` que define el estado actual. El método `solicitar` desencadena la transición de estado.

## Uso

Ejecuta el script para simular las transiciones de estado en un repositorio Git:

```python
if __name__ == "__main__":
    contexto = Contexto()
    
    # Simulamos el ciclo de estados en git
    print("Estado inicial:")
    contexto.solicitar()  # No hay cambios en el repositorio.
    
    print("\nRealizando cambios en el repositorio:")
    contexto.solicitar()  # Agregando cambios al repositorio.
    
    print("\nEjecutando 'git add':")
    contexto.solicitar()  # Los cambios están en el área de stage.
    
    print("\nEjecutando 'git commit':")
    contexto.solicitar()  # Los cambios han sido commiteados.
    
    print("\nEstado final:")
    contexto.solicitar()  # No hay cambios en el repositorio.

```

## Salida

```bash
Estado inicial:
No hay cambios en el repositorio.

Realizando cambios en el repositorio:
Agregando cambios al repositorio.

Ejecutando 'git add':
Los cambios están en el área de stage.

Ejecutando 'git commit':
Los cambios han sido commiteados.

Estado final:
No hay cambios en el repositorio.
```

## Conclusión

El patrón State es útil cuando un objeto debe cambiar su comportamiento en función de su estado interno. En este caso, el patrón State se utilizó para simular los estados de un repositorio Git. Cada estado tiene su propia clase y maneja la transición al siguiente estado.
```