# 🔌 Patrón Adapter: Sistema Flexible de Almacenamiento y Notificaciones

## 🎯 Objetivo del Proyecto

Demostrar la implementación del **Patrón Adapter** utilizando un sistema de almacenamiento y notificaciones multiplataforma.

## 🧩 Patrón Adapter: Explicación Conceptual

### ¿Qué es el Patrón Adapter?

El Patrón Adapter es un patrón de diseño estructural que permite que interfaces incompatibles trabajen juntas. Actúa como un traductor entre dos objetos con interfaces diferentes.

### Componentes Clave

1. **Target (Interfaz Objetivo)**: 
   - Define la interfaz que el cliente espera utilizar
   - `AlmacenamientoTarget`
   - `NotificacionTarget`

2. **Adaptee (Servicio Existente)**: 
   - Clase con una interfaz diferente que necesita ser adaptada
   - `GoogleDrive`, `Dropbox`, `S3`
   - `Mail`, `WhatsApp`, `Telegram`

3. **Adapter (Adaptador)**:
   - Implementa la interfaz del Target
   - Envuelve un Adaptee
   - `GoogleDriveAdapter`, `DropboxAdapter`, `S3Adapter`
   - `MailAdapter`, `WhatsAppAdapter`, `TelegramAdapter`


## 🚀 Características del Sistema

### Almacenamiento Multiplataforma
- Soporta diferentes servicios de almacenamiento:
  - Google Drive
  - Dropbox
  - Amazon S3

### Notificaciones Multiplataforma
- Envío de notificaciones por:
  - Email
  - WhatsApp
  - Telegram

## 💡 Beneficios del Patrón Adapter

1. **Desacoplamiento**
   - Separa la lógica del cliente de las implementaciones específicas
   - Facilita la integración de nuevos servicios

2. **Flexibilidad**
   - Permite cambiar servicios sin modificar el código cliente
   - Añade nuevas implementaciones con mínimo esfuerzo

3. **Reutilización**
   - Aprovecha código existente
   - Evita reescribir funcionalidades

## 🔍 Ejemplo de Uso

```python
# Crear cliente con Google Drive y WhatsApp
cliente1 = Cliente(GoogleDriveAdapter(), WhatsAppAdapter())
cliente1.guardar_archivo("documento.txt", contenido)
cliente1.enviar_notificacion("Archivo guardado")

# Cambiar a Dropbox y Telegram sin modificar código
cliente2 = Cliente(DropboxAdapter(), TelegramAdapter())
cliente2.guardar_archivo("informe.pdf", contenido)
cliente2.enviar_notificacion("Informe listo")
```

## 🛠️ Implementación Detallada

### Interfaces Target
```python
class AlmacenamientoTarget(ABC):
    @abstractmethod
    def guardar_archivo(self, archivo: str, contenido: Any) -> bool:
        pass

class NotificacionTarget(ABC):
    @abstractmethod
    def enviar_notificacion(self, mensaje: str) -> bool:
        pass
```

### Adapter Típico
```python
class GoogleDriveAdapter(AlmacenamientoTarget):
    def __init__(self):
        self.drive = GoogleDrive()

    def guardar_archivo(self, archivo: str, contenido: Any) -> bool:
        return self.drive.subir_a_drive(archivo, contenido)
```

## 🌟 Casos de Uso Reales

- Integración de sistemas heredados
- Conectar servicios de diferentes proveedores
- Migración entre plataformas
- Desarrollo de aplicaciones escalables

## 🚧 Extensibilidad

Añadir nuevos servicios:
1. Crear clase de servicio externa
2. Implementar adaptador que herede de `AlmacenamientoTarget` o `NotificacionTarget`
3. Usar en el cliente

## Resultado Esperado

```	bash
Subiendo archivo.txt a Google Drive
Enviando WhatsApp: Mensaje de prueba
Subiendo archivo.txt a Dropbox
Broadcasting en Telegram: Mensaje de prueba
Subiendo archivo.txt a Dropbox
Enviando WhatsApp: Mensaje de prueba
Subiendo archivo.txt a S3
Envío de Email: Mensaje de prueba
```
