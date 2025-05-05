# Gestor de Tareas (ToDo API)

**Este proyecto no tiene otra finalidad mas que el estudio de Django y
Django Rest Framework**

## Descripción
Este proyecto es una API RESTful que permite a los usuarios gestionar sus tareas personales. Cada usuario puede crear tareas con título, descripción, fecha límite y estado (completada o no). La API protege las rutas con autenticación JWT, asegurando que solo el dueño de una tarea pueda modificarla o eliminarla.

## Funcionalidades
- **Registro y login de usuario:** Los usuarios pueden registrarse y autenticarse usando JWT.
- **CRUD de tareas:** Los usuarios pueden crear, leer, actualizar y eliminar solo sus propias tareas.
- **Autenticación JWT:** Las rutas están protegidas mediante autenticación basada en tokens JWT.
- **Filtrado por usuario:** Los usuarios solo pueden ver, editar y eliminar tareas que les pertenezcan.
- **Manejo de errores estándar:** Si un usuario intenta acceder a una tarea que no le pertenece o no existe, se devuelve un error 404 o 403.

## Tecnologías Usadas
- **Django**: Framework de Python para el backend.
- **Django REST Framework**: Para crear la API RESTful.
- **JWT**: JSON Web Token para autenticación.
- **PostgreSQL**: Base de datos relacional.
- **drf-yasg**: Generación automática de documentación Swagger para la API.
