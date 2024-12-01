class Estado:
    def manejar(self, contexto):
        raise NotImplementedError("Debe implementar el método manejar")

class EstadoSinCambios(Estado):
    def manejar(self, contexto):
        print("No hay cambios en el repositorio.")
        contexto.estado = EstadoAgregarCambios()

class EstadoAgregarCambios(Estado):
    def manejar(self, contexto):
        print("Agregando cambios al repositorio.")
        contexto.estado = EstadoStaged()

class EstadoStaged(Estado):
    def manejar(self, contexto):
        print("Los cambios están en el área de stage.")
        contexto.estado = EstadoCommit()

class EstadoCommit(Estado):
    def manejar(self, contexto):
        print("Los cambios han sido commiteados.")
        contexto.estado = EstadoSinCambios()

class Contexto:
    def __init__(self):
        self.estado = EstadoSinCambios()

    def solicitar(self):
        self.estado.manejar(self)

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