
# Flask CRUD Application

Esta es una aplicación web CRUD (Crear, Leer, Actualizar, Eliminar) desarrollada utilizando **Python** y **Flask**. La aplicación permite a los usuarios gestionar una lista de registros (nombre y correo electrónico) almacenados en una base de datos **SQLite**.

## Características

- **Crear**: Permite a los usuarios añadir nuevos registros a la base de datos.
- **Leer**: Muestra todos los registros en una tabla con una estructura clara.
- **Actualizar**: Permite a los usuarios editar los registros existentes.
- **Eliminar**: Permite a los usuarios eliminar registros de la base de datos.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal para la lógica de la aplicación.
- **Flask**: Framework utilizado para crear el servidor web y manejar las rutas.
- **SQLite**: Base de datos ligera utilizada para almacenar los datos.
- **HTML/CSS**: Para el diseño y la estructura de la interfaz de usuario.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:
```
flask-crud-app/
├── app.py             # Código principal de la aplicación Flask
├── templates/
│   ├── index.html     # Plantilla HTML para la interfaz de usuario
└── database.db        # Archivo de base de datos SQLite
```

## Instalación y Configuración

Sigue estos pasos para configurar y ejecutar la aplicación en tu entorno local:

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/flask-crud-app.git
   ```

2. **Navega al directorio del proyecto**:
   ```bash
   cd flask-crud-app
   ```

3. **Crea y activa un entorno virtual (opcional pero recomendado)**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # En Windows usa `venv\Scripts\activate`
   ```

4. **Instala las dependencias**:
   ```bash
   pip install flask
   ```

5. **Ejecuta la aplicación**:
   ```bash
   python app.py
   ```

6. Abre tu navegador web y navega a `http://localhost:5000` para ver la aplicación en funcionamiento.

## Uso

1. **Crear un nuevo registro**:
   - Completa los campos "Name" y "Email" en el formulario.
   - Haz clic en el botón "Add User" para añadir el nuevo registro a la base de datos.

2. **Editar un registro existente**:
   - Haz clic en el botón "Edit" junto al registro que deseas modificar.
   - Modifica los datos en el formulario y guarda los cambios.

3. **Eliminar un registro**:
   - Haz clic en el botón "Delete" junto al registro que deseas eliminar.
   - El registro será eliminado de la base de datos.

## Base de Datos

La aplicación utiliza **SQLite**, una base de datos ligera y fácil de usar que está integrada en Python. El archivo de la base de datos se crea automáticamente si no existe.

## Mejoras Futuras

Algunas mejoras que podrían implementarse en el futuro incluyen:
- **Autenticación de usuarios** para limitar el acceso a las operaciones CRUD.
- **Paginación y búsqueda** en la tabla de usuarios para facilitar la gestión de grandes volúmenes de datos.
- **Validación de formularios** avanzada y manejo de errores en la interfaz de usuario.
- **Despliegue** en un servidor web como Heroku o DigitalOcean para hacer la aplicación accesible en línea.

## Contribuciones

Las contribuciones son bienvenidas. Si tienes alguna sugerencia o deseas mejorar esta aplicación, no dudes en enviar un pull request o abrir un issue en el repositorio.

## Licencia

Este proyecto está bajo la Licencia MIT. Puedes utilizar, modificar y distribuir este proyecto con total libertad.
