import copy

class Naruto:
    def __init__(self, nombre, nivel_chakra):
        self.nombre = nombre
        self.nivel_chakra = nivel_chakra

    def clonar(self):
        # Utiliza deepcopy para crear una copia profunda del objeto
        return copy.deepcopy(self)

    def __str__(self):
        return f"Naruto(nombre={self.nombre}, nivel_chakra={self.nivel_chakra})"

# Crear un objeto original de Naruto
naruto_original = Naruto("Naruto Uzumaki", 100)

print("Original: ", naruto_original, "- Dir de memoria: ", id(naruto_original))
print("\nCreando clones 5 de sombra:")

# Crear 5 clones de sombra
clones_sombra = [naruto_original.clonar() for _ in range(5)]
# Modificar el nivel de chakra de los clones de sombra descendiendo en 25 
for i, clone in enumerate(clones_sombra):
    clone.nivel_chakra -= 25
    print(f"Clone {i+1}: {clone} - Dir de memoria: {id(clone)}")


