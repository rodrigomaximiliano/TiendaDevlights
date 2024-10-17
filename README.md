### Tienda Devlights

### Proyecto final del bootcamp DevLights 3.0

Alumnos:

    Otto Silva
    Facundo Falcone
    Rodrigo Maximiliano Portillo

Este proyecto es una tienda que está dividido en dos partes: el backend, que utiliza FastAPI conectado a una base de datos MongoDB, y el frontend, que utiliza Vue. A continuación, se describen los pasos necesarios para clonar el proyecto y ejecutarlo en tu máquina local.
Requisitos Previos

Antes de comenzar, asegúrate de tener instalados los siguientes programas:

    Python (3.7 o superior)
    Node.js y npm
    Git

Clona o Forkea el proyecto

Navegar a la Carpeta del Proyecto entra en la carpeta del proyecto:

    cd Store-App

Configuración del Backend navegar a la Carpeta del Backend:

cd backend-fastApi

Crear un Entorno Virtual

python -m venv venv

Activar el Entorno Virtual

    En Windows:

.\venv\Scripts\Activate.ps1


En macOS/Linux:

    source venv/bin/activate

Instalar Dependencias
Instala las dependencias necesarias ejecutando:

pip install -r requirements.txt

Configura el archivo .env con la conexión a tu base de datos.

Ejecutar el Backend

Inicia el servidor de FastAPI:

    uvicorn app.main:app --reload

    El backend estará disponible en http://127.0.0.1:8000.

Configuración del Frontend: navegar a la Carpeta del Frontend

cd ../frontend-vue

Instalar Dependencias
Ejecuta el siguiente comando para instalar las dependencias del frontend:
npm install

Inicia el servidor de desarrollo de Vue.js: npm run serve

    El frontend estará disponible en http://localhost:8080.

Probar el Proyecto
Asegúrate de que ambos servidores (backend y frontend) estén corriendo al mismo tiempo.
Si encuentras errores, verifica que todas las dependencias estén correctamente instaladas y que las rutas en los archivos de configuración sean correctas.
