
from abc import ABC, abstractmethod
from typing import Any

# Interfaces abstractas
class AlmacenamientoTarget(ABC):
    @abstractmethod
    def guardar_archivo(self, archivo: str, contenido: Any) -> bool:
        pass

class NotificacionTarget(ABC):
    @abstractmethod
    def enviar_notificacion(self, mensaje: str) -> bool:
        pass

# Servicios externos (simulados)
class GoogleDrive:
    def subir_a_drive(self, nombre: str, datos: Any) -> bool:
        print(f"Subiendo {nombre} a Google Drive")
        return True

class Dropbox:
    def upload_file(self, file_name: str, data: Any) -> bool:
        print(f"Subiendo {file_name} a Dropbox")
        return True

class S3:
    def upload_file(self, file_name: str, data: Any) -> bool:
        print(f"Subiendo {file_name} a S3")
        return True
      
class Mail:
    def send_mail(self, subject: str, body: str) -> bool:
        print(f"Enviando mail: {subject}")
        return True

class WhatsApp:
    def send_message(self, text: str) -> bool:
        print(f"Enviando WhatsApp: {text}")
        return True

class Telegram:
    def broadcast(self, content: str) -> bool:
        print(f"Broadcasting en Telegram: {content}")
        return True

# Adaptadores
class GoogleDriveAdapter(AlmacenamientoTarget):
    def __init__(self):
        self.drive = GoogleDrive()

    def guardar_archivo(self, archivo: str, contenido: Any) -> bool:
        return self.drive.subir_a_drive(archivo, contenido)

class DropboxAdapter(AlmacenamientoTarget):
    def __init__(self):
        self.dropbox = Dropbox()

    def guardar_archivo(self, archivo: str, contenido: Any) -> bool:
        return self.dropbox.upload_file(archivo, contenido)
      
class S3Adapter(AlmacenamientoTarget):
    def __init__(self):
        self.s3 = S3()

    def guardar_archivo(self, archivo: str, contenido: Any) -> bool:
        return self.s3.upload_file(archivo, contenido)
      
class MailAdapter(NotificacionTarget):
    def __init__(self):
        self.mail = Mail()

    def enviar_notificacion(self, mensaje: str) -> bool:
        return self.mail.send_mail("Notificación", mensaje)

class WhatsAppAdapter(NotificacionTarget):
    def __init__(self):
        self.whatsapp = WhatsApp()

    def enviar_notificacion(self, mensaje: str) -> bool:
        return self.whatsapp.send_message(mensaje)

class TelegramAdapter(NotificacionTarget):
    def __init__(self):
        self.telegram = Telegram()

    def enviar_notificacion(self, mensaje: str) -> bool:
        return self.telegram.broadcast(mensaje)
      
      
# Cliente

class Cliente:
    def __init__(self, almacenamiento: AlmacenamientoTarget, notificacion: NotificacionTarget):
        self.almacenamiento = almacenamiento
        self.notificacion = notificacion

    def guardar_archivo(self, archivo: str, contenido: Any) -> bool:
        return self.almacenamiento.guardar_archivo(archivo, contenido)

    def enviar_notificacion(self, mensaje: str) -> bool:
        return self.notificacion.enviar_notificacion(mensaje)
      
# Uso

if __name__ == "__main__":
    cliente1 = Cliente(GoogleDriveAdapter(), WhatsAppAdapter())
    cliente1.guardar_archivo("archivo.txt", "contenido")
    cliente1.enviar_notificacion("Mensaje de prueba")

    cliente2 = Cliente(DropboxAdapter(), TelegramAdapter())
    cliente2.guardar_archivo("archivo.txt", "contenido")
    cliente2.enviar_notificacion("Mensaje de prueba")
    
    cliente3 = Cliente(DropboxAdapter(), WhatsAppAdapter())
    cliente3.guardar_archivo("archivo.txt", "contenido")
    cliente3.enviar_notificacion("Mensaje de prueba")
    
    cliente4 = Cliente(S3Adapter(), MailAdapter())
    cliente4.guardar_archivo("archivo.txt", "contenido")
    cliente4.enviar_notificacion("Mensaje de prueba")
    
    
  