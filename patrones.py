"""
Código Base - Motor de Plataforma de Publicaciones
El estudiante debe completar las secciones marcadas con [TAREA]
"""
from abc import ABC, abstractmethod
from typing import List

# ==========================================
# PATRÓN FACTORY METHOD (Creación de Contenido)
# ==========================================

# 1. Interfaz base para todas las publicaciones
class Publicacion(ABC):
    def __init__(self, titulo: str, contenido: str):
        self.titulo = titulo
        self.contenido = contenido

    @abstractmethod
    def mostrar(self):
        pass

# [TAREA 1] Implementar clases concretas: 'Articulo' (formato largo) y 'PostCorto' (formato breve)
class Articulo(Publicacion):
    def mostrar(self):
        # El estudiante debe formatear la salida simulando un artículo completo
        print(f"--- ARTÍCULO ---\nTítulo: {self.titulo}\nContenido Completo: {self.contenido}\n----------------")

class PostCorto(Publicacion):
    def mostrar(self):
        # El estudiante debe formatear la salida simulando un post rápido
        print(f"[POST CORTA] {self.titulo} - {self.contenido[:20]}...")

# [TAREA 2] Implementar la Fábrica
class FabricaPublicaciones:
    @staticmethod
    def crear_publicacion(tipo: str, titulo: str, contenido: str) -> Publicacion:
        """
        El estudiante debe retornar la instancia adecuada según el 'tipo' 
        ('articulo' o 'post'). Debe manejar tipos desconocidos con un ValueError.
        """
        if tipo.lower() == 'articulo':
            return Articulo(titulo, contenido)
        elif tipo.lower() == 'post':
            return PostCorto(titulo, contenido)
        else:
            raise ValueError(f"Tipo de publicación '{tipo}' no soportado.")

# ==========================================
# PATRÓN OBSERVER (Sistema de Notificaciones)
# ==========================================

# [TAREA 3] Implementar la interfaz del Observador (Lector)
class Observador(ABC):
    @abstractmethod
    def actualizar(self, mensaje: str):
        pass

# [TAREA 4] Implementar el Sujeto (Autor) que notificará a los observadores
class Autor:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.seguidores: List[Observador] = []

    def agregar_seguidor(self, lector: Observador):
        self.seguidores.append(lector)
        print(f"Sistema: Un nuevo lector ha seguido a {self.nombre}.")

    def remover_seguidor(self, lector: Observador):
        self.seguidores.remove(lector)

    def notificar_seguidores(self, titulo_publicacion: str):
        """
        El estudiante debe iterar sobre la lista de seguidores y llamar a su método actualizar().
        """
        mensaje = f"¡El autor {self.nombre} ha publicado un nuevo contenido: '{titulo_publicacion}'!"
        for seguidor in self.seguidores:
            seguidor.actualizar(mensaje)

    def publicar(self, tipo: str, titulo: str, contenido: str):
        # Uso de la Fábrica para crear el contenido
        nueva_publicacion = FabricaPublicaciones.crear_publicacion(tipo, titulo, contenido)
        nueva_publicacion.mostrar()
        
        # Uso del Observer para notificar
        self.notificar_seguidores(titulo)

# Clase concreta de Observador
class Lector(Observador):
    def __init__(self, nombre: str):
        self.nombre = nombre

    def actualizar(self, mensaje: str):
        print(f"Notificación para {self.nombre}: {mensaje}")

# ==========================================
# SIMULACIÓN (Bloque de ejecución)
# ==========================================
if __name__ == "__main__":
    print("Iniciando Motor de Publicaciones...\n")
    
    # 1. Creación del Autor y Lectores
    autor = Autor("Ada Lovelace")
    lector1 = Lector("Carlos")
    lector2 = Lector("María")
    
    # 2. Suscripción
    autor.agregar_seguidor(lector1)
    autor.agregar_seguidor(lector2)
    print("\n")
    
    # 3. Publicación de Contenido
    autor.publicar("articulo", "El futuro del código", "Los algoritmos dominarán la optimización de procesos...")
    print("\n")
    autor.publicar("post", "¡Hola mundo!", "Este es mi primer post en la plataforma. ¡Saludos!")
