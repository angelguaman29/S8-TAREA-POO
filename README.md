# Cambios Realizados

## Objetivo

Cambios realizados en el archivo `Dashboard.py` original para mejorar su estructura usando buenas prácticas de programación, modularidad y clases.

---

## ¿Qué cambios se hicieron?

### 1. Crear carpeta "modelos"

**Archivos creados:**
- `modelos/menu.py` - Clase Menu
- `modelos/proyecto.py` - Clase Proyecto

**Por qué:** Separar el código en clases hace más fácil entender y mantener.

---

### 2. Crear carpeta "servicios"

**Qué es:** Carpeta que contiene las clases que hacen las operaciones.

**Archivos creados:**
- `servicios/gestor_proyectos.py` - Clase GestorProyectos

**Por qué:** La lógica del programa está separada de la representación de datos.

---

### 3. Crear clase Menu

**Responsabilidad:** Mostrar menús interactivos.

**Métodos:**
- `__init__()` - Inicializa el menu
- `agregar_opcion()` - Agrega una opcion al menu
- `mostrar()` - Muestra el menu en pantalla
- `obtener_opciones()` - Retorna las opciones

**Beneficio:** No hay que repetir código para mostrar menús.

---

### 4. Crear clase Proyecto

**Responsabilidad:** Representar un proyecto.

**Métodos:**
- `__init__()` - Inicializa el proyecto
- `obtener_nombre()` - Retorna el nombre
- `obtener_descripcion()` - Retorna la descripcion
- `obtener_ruta()` - Retorna la ruta
- `mostrar_informacion()` - Muestra información

**Beneficio:** Cada proyecto es un objeto reutilizable.

---

### 5. Crear clase GestorProyectos

**Responsabilidad:** Gestionar la colección de proyectos.

**Métodos:**
- `__init__()` - Inicializa el gestor
- `agregar_proyecto()` - Agrega un proyecto
- `obtener_todos_proyectos()` - Retorna todos los proyectos
- `contar_proyectos()` - Cuenta los proyectos
- `buscar_por_nombre()` - Busca un proyecto por nombre
- `listar_proyectos()` - Lista todos los proyectos

**Beneficio:** Toda la lógica de gestión está en un solo lugar.

---

### 6. Actualizar Dashboard.py

**Cambios:**
- Ahora usa las clases creadas
- Código más limpio y organizado
- Menos código repetido
- Más fácil de mantener

**Antes:** Todo el código mezclado en un archivo.
**Después:** Código organizado en clases.

---

## Estructura final

```
S8-TAREA-POO/
├── modelos/
│   ├── __init__.py
│   ├── menu.py
│   └── proyecto.py
├── servicios/
│   ├── __init__.py
│   └── gestor_proyectos.py
├── UNIDAD 1/
├── UNIDAD 2/
├── Dashboard.py (actualizado)
└── README.md (actualizado)
```

---

## Ventajas de los cambios

✓ **Modularidad** - Código separado en clases
✓ **Reutilización** - Las clases se pueden usar en otros proyectos
✓ **Mantenibilidad** - Fácil de entender y modificar
✓ **Escalabilidad** - Fácil de agregar nuevas funcionalidades
✓ **Buenas prácticas** - Sigue estándares profesionales

---

## Cómo usar el Dashboard

1. Ejecutar el programa:
   ```bash
   python Dashboard.py
   ```

2. Seleccionar una opcion del menu

3. Ver la informacion de los proyectos

---
