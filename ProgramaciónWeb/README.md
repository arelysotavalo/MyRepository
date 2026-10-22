# Programacion Web 

## Objetivo del Proyecto
Desarrollar y desplegar un sitio web de perfil profesional interactivo y responsivo usando HTML y CSS, aplicando buenas prácticas de maquetación web y creando contenedores en Docker de manera correcta.

--------

## Tecnologías Utilizadas
* **Inteligencia Artificial (IA)**: Utilizada para el diseño y generación del mockup de alta fidelidad del sitio web.
* **HTML5**: Estructuración semántica del contenido del sitio web.
* **CSS**: Estilos personalizados y diseño general de la interfaz
* **Nginx**: Servidor web de alto rendimiento utilizado para servir la aplicación estática.
* **Docker**: Creación de contenedores para la aplicación, garantizando un entorno de ejecución portátil y consistente.
* **Git & GitHub**: Control de versiones y repositorio del código fuente.

--------

##  Estructura del Proyecto
La estructura de directorios y archivos del proyecto se organiza de la siguiente manera:

```text
MyRepository/
│
├── POO
|
├── DesarrolloWeb/
│   ├── index.html        # Página principal con la estructura semántica HTML5
│   ├── estilos.css       # Hoja de estilos externa para el diseño y formato visual
│   ├── Espe.png          # Imagen institucional / logotipo
│   ├── FotoPerfil.png    # Fotografía de perfil profesional
│   ├── EURACE.png        # Insignia o imagen adicional del carrusel
│   ├── Docker            # Configuración para empaquetar la aplicación en Docker con Nginx
│   └── README.md         # Documentación oficial del proyecto

```
Adicionalmente, en la codificación del archivo principal se implementaron las directrices de maquetación semántica de **HTML5**, utilizando etiquetas estructurales como `<header>`, `<nav>`, `<section>` y `<footer>`. Esto permite una mejor organización del contenido, facilita la accesibilidad y optimiza la lectura e interpretación del código fuente por parte de los navegadores y motores de búsqueda.

--------

##  Instrucciones para Construir y Ejecutar la Imagen Docker
Para desplegar este proyecto localmente utilizando la creación de contenedores con Docker y Nginx, se siguió los pasos a continuaión:

### 1. Requisitos previos
* Tener instalado **Docker** en la computadora y asegurarse de que el servicio esté activo (Docker Desktop / WSL 2).

### 2. Verificar o crear el archivo `Dockerfile`
Asegurarse de que en la misma carpeta donde se encuentra el archivo `index.html` y `estilos.css` exista un archivo llamado **`Dockerfile`** (sin extensión) con la siguiente configuración:

```dockerfile
FROM nginx:alpine

# Copiar todos los archivos y recursos necesarios (HTML, CSS y multimedia) para visualizar la página web completa en Nginx
COPY . /usr/share/nginx/html

EXPOSE 80
```
### 3. Construir la imagen de Docker
Abrir una terminal (PowerShell, CMD o Terminal) en la ruta raíz del proyecto donde se encuentra el archivo `Dockerfile` y ejecutar el siguiente comando para construir la imagen:

```bash
docker build -t perfil-html-css .
```
### Ejecución del Contenedor
Una vez construida la imagen, lanzar el contenedor vinculando el puerto 8080 de la máquina anfitriona (host) con el puerto 80 del contenedor Nginx:

```bash
docker run -d -p 8080:80 --name mi-contenedor perfil-html-css
```
### Verificación
Abrir un navegador web e ingresar a la siguiente dirección para visualizar la página en funcionamiento:

```bash
http://localhost:8080
```
----
##  Enlace a Docker Hub

https://hub.docker.com/r/arelysotavalo/programacionweb




