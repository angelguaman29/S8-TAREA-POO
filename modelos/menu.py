#Clase  gestiona los menus interactivos

class Menu:
    """
    Crear y mostrar menus.
    Esta clase permite separar la logica del menu del Dashboard principal.
    """
    
    def __init__(self, titulo):
        """
        Constructor que inicializa el menu.
        
        Parametro:
        - titulo: el titulo que tendra el menu (string)
        """
        # Guardar el titulo del menu
        self.titulo = titulo
        
        # Diccionario para almacenar las opciones del menu
        # Ejemplo: {'1': 'Unidad 1', '2': 'Unidad 2'}
        self.opciones = {}
    
    
    def agregar_opcion(self, numero, descripcion):
        """
        Agregar una opcion al menu.
        
        Parametros:
        - numero: el numero de la opcion (string o int)
        - descripcion: lo que dice la opcion (string)
        """
        # Convertir numero a string por si acaso
        numero = str(numero)
        
        # Agregar la opcion al diccionario
        self.opciones[numero] = descripcion
    
    
    def mostrar(self):
        """
        Mostrar el menu en pantalla.
        Muestra el titulo y todas las opciones agregadas.
        """
        print("\n" + "=" * 60)
        print(self.titulo)
        print("=" * 60)
        
        # Recorrer todas las opciones y mostrarlas
        for numero in sorted(self.opciones.keys()):
            descripcion = self.opciones[numero]
            print(f"{numero} - {descripcion}")
        
        print("=" * 60)
    
    
    def obtener_opciones(self):
        """
        Retorna todas las opciones del menu.
        
        Retorna: diccionario con las opciones
        """
        return self.opciones