# Clase que representa un proyecto

class Proyecto:
    """
    Clase  representa un proyecto de POO.
    Almacena informacion basica de un proyecto.
    """
    
    def __init__(self, nombre, descripcion, ruta):
        """
        Constructor que inicializa un proyecto.
        
        Parametros:
        - nombre: nombre del proyecto (string)
        - descripcion: descripcion de que hace el proyecto (string)
        - ruta: ruta donde esta ubicado el proyecto (string)
        """
        # Guardar el nombre del proyecto
        self.nombre = nombre
        
        # Guardar la descripcion del proyecto
        self.descripcion = descripcion
        
        # Guardar la ruta del proyecto
        self.ruta = ruta
    
    
    def obtener_nombre(self):
        """
        Retorna el nombre del proyecto.
        
        Retorna: nombre del proyecto (string)
        """
        return self.nombre
    
    
    def obtener_descripcion(self):
        """
        Retorna la descripcion del proyecto.
        
        Retorna: descripcion del proyecto (string)
        """
        return self.descripcion
    
    
    def obtener_ruta(self):
        """
        Retorna la ruta del proyecto.
        
        Retorna: ruta del proyecto (string)
        """
        return self.ruta
    
    
    def mostrar_informacion(self):
        """
        Muestra toda la informacion del proyecto.
        """
        print(f"\nNombre: {self.nombre}")
        print(f"Descripcion: {self.descripcion}")
        print(f"Ruta: {self.ruta}")