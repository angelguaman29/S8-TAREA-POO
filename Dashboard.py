# Archivo principal que ejecuta el dashboard
# # Utiliza las clases de modelos y servicios para funcionar.

# Importar las clases creadas
import os
import subprocess
from modelos.menu import Menu
from modelos.proyecto import Proyecto
from servicios.gestor_proyectos import GestorProyectos


class Dashboard:
    """
    Clase principal que gestiona el dashboard.
    Coordina todas las clases para funcionar juntas.
    """
    
    def __init__(self):
        """
        Constructor que inicializa el dashboard.
        """
        # Crear el gestor de proyectos
        self.gestor = GestorProyectos()
        
        # Obtener la ruta donde esta el dashboard
        self.ruta_base = os.path.dirname(__file__)
        
        # Cargar los proyectos disponibles
        self.cargar_proyectos()
    
    
    def cargar_proyectos(self):
        """
        Metodo que carga los proyectos desde las carpetas.
        Busca las carpetas UNIDAD 1 y UNIDAD 2.
        """
        # Rutas donde estan las unidades
        ruta_unidad1 = os.path.join(self.ruta_base, "UNIDAD 1")
        ruta_unidad2 = os.path.join(self.ruta_base, "UNIDAD 2")
        
        # Si existen las carpetas, cargar los proyectos
        if os.path.exists(ruta_unidad1):
            # Crear proyecto para Unidad 1
            proyecto1 = Proyecto(
                "UNIDAD 1",
                "Ejemplos basicos de Programacion Orientada a Objetos",
                ruta_unidad1
            )
            self.gestor.agregar_proyecto(proyecto1)
        
        if os.path.exists(ruta_unidad2):
            # Crear proyecto para Unidad 2
            proyecto2 = Proyecto(
                "UNIDAD 2",
                "Ejemplos avanzados de Programacion Orientada a Objetos",
                ruta_unidad2
            )
            self.gestor.agregar_proyecto(proyecto2)
    
    
    def mostrar_menu_principal(self):
        """
        Metodo que muestra el menu principal.
        Utiliza la clase Menu para mostrar las opciones.
        """
        # Crear el menu principal
        menu = Menu("MI DASHBOARD DE PROGRAMACION ORIENTADA A OBJETOS")
        
        # Agregar opciones al menu
        menu.agregar_opcion("1", "UNIDAD 1")
        menu.agregar_opcion("2", "UNIDAD 2")
        menu.agregar_opcion("3", "Ver todos los proyectos")
        menu.agregar_opcion("0", "Salir")
        
        # Mostrar el menu
        menu.mostrar()
    
    
    def mostrar_codigo(self, ruta_script):
        """
        Metodo que muestra el contenido de un archivo.
        
        Parametro:
        - ruta_script: ruta del archivo a mostrar
        """
        # Obtener la ruta absoluta del archivo
        ruta_absoluta = os.path.abspath(ruta_script)
        
        try:
            # Abrir el archivo en modo lectura
            with open(ruta_absoluta, 'r') as archivo:
                # Leer el contenido
                codigo = archivo.read()
                
                # Mostrar el contenido
                print(f"\n--- Codigo de {ruta_script} ---\n")
                print(codigo)
                
                return codigo
        
        except FileNotFoundError:
            print("El archivo no se encontro.")
            return None
        
        except Exception as e:
            print(f"Ocurrio un error al leer el archivo: {e}")
            return None
    
    
    def ejecutar_codigo(self, ruta_script):
        """
        Metodo que ejecuta un archivo Python.
        
        Parametro:
        - ruta_script: ruta del archivo a ejecutar
        """
        try:
            # Verificar si es Windows o Linux/Mac
            if os.name == 'nt':  # Windows
                # Abrir cmd para ejecutar el script
                subprocess.Popen(['cmd', '/k', 'python', ruta_script])
            else:  # Linux/Mac
                # Abrir terminal para ejecutar el script
                subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
        
        except Exception as e:
            print(f"Ocurrio un error al ejecutar el codigo: {e}")
    
    
    def ejecutar(self):
        """
        Metodo principal que ejecuta el dashboard.
        Muestra el menu y coordina todas las acciones.
        """
        print("="*60)
        print("BIENVENIDO AL DASHBOARD ")
        print("UEA")
        print("="*60)
        
        # Variable para controlar el bucle
        activo = True
        
        while activo:
            # Mostrar el menu principal
            self.mostrar_menu_principal()
            
            # Pedir la opcion al usuario
            opcion = input("\nSeleccione una opcion: ")
            
            # Procesar la opcion seleccionada
            if opcion == "1":
                # Mostrar Unidad 1
                proyecto = self.gestor.buscar_por_nombre("UNIDAD 1")
                if proyecto:
                    proyecto.mostrar_informacion()
            
            elif opcion == "2":
                # Mostrar Unidad 2
                proyecto = self.gestor.buscar_por_nombre("UNIDAD 2")
                if proyecto:
                    proyecto.mostrar_informacion()
            
            elif opcion == "3":
                # Listar todos los proyectos
                self.gestor.listar_proyectos()
            
            elif opcion == "0":
                # Salir del programa
                print("\nGracias por usar el Dashboard. ¡Hasta luego!")
                activo = False
            
            else:
                print("\nOpcion no valida. Por favor intente de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    # Crear el dashboard
    dashboard = Dashboard()
    
    # Ejecutar el dashboard
    dashboard.ejecutar()