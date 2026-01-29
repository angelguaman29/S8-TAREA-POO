# Clase que gestiona los proyectos

class GestorProyectos:
    """
    Clase que gestiona una coleccion de proyectos.
    Permite agregar, buscar y obtener informacion de proyectos.
    """
    
    def __init__(self):
        """
        Inicializa el gestor.
        Crea una lista vacia para almacenar los proyectos.
        """
        # Lista privada para almacenar los proyectos
        self._proyectos = []
    
    
    def agregar_proyecto(self, proyecto):
        """
        Agregar un proyecto a la lista.
        
        Parametro:
        - proyecto: objeto de tipo Proyecto
        """
        # Agregar el proyecto a la lista
        self._proyectos.append(proyecto)
        
        # Mensaje de confirmacion
        print(f"Proyecto '{proyecto.obtener_nombre()}' agregado correctamente.")
    
    
    def obtener_todos_proyectos(self):
        """
        Retorna todos los proyectos.
        
        Retorna: lista con todos los proyectos
        """
        return self._proyectos
    
    
    def contar_proyectos(self):
        """
        Cuenta cuantos proyectos hay.
        
        Retorna: numero de proyectos (integer)
        """
        return len(self._proyectos)
    
    
    def buscar_por_nombre(self, nombre):
        """
        Busca un proyecto por su nombre.
        
        Parametro:
        - nombre: nombre del proyecto a buscar (string)
        
        Retorna: el proyecto si lo encuentra, None si no existe
        """
        # Recorrer la lista de proyectos
        for proyecto in self._proyectos:
            # Si el nombre coincide (sin importar mayusculas/minusculas)
            if proyecto.obtener_nombre().lower() == nombre.lower():
                # Retornar el proyecto encontrado
                return proyecto
        
        # Si no encuentra el proyecto, retorna None
        return None
    
    
    def listar_proyectos(self):
        """
        Muestra todos los proyectos en formato de lista.
        """
        if self.contar_proyectos() == 0:
            print("No hay proyectos registrados.")
        else:
            print("\n--- LISTA DE PROYECTOS ---")
            for i, proyecto in enumerate(self._proyectos, 1):
                print(f"{i}. {proyecto.obtener_nombre()} - {proyecto.obtener_descripcion()}")