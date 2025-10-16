Gestor de Transporte - TransiTrack API 🚌
API RESTful desarrollada con Django y Django REST Framework para la gestión simple de rutas de transporte y los conductores asignados a ellas.

✨ Tecnologías Usadas
Python

Django

Django REST Framework

SQLite3 (Base de datos por defecto)

🚀 Instalación y Ejecución
Sigue estos pasos para levantar el servidor en tu entorno local.

Clona el repositorio:

Bash
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
cd TU_REPOSITORIO
Crea y activa un entorno virtual:

Bash
# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Para Windows
python -m venv venv
.\venv\Scripts\activate
Instala las dependencias:

Bash
pip install -r requirements.txt
Aplica las migraciones a la base de datos:

Bash
python manage.py migrate
Inicia el servidor de desarrollo:

Bash
python manage.py runserver
La API estará disponible en http://127.0.0.1:8000/api/v1/.

🕹️ Endpoints Disponibles
A continuación se detallan los endpoints de la API y cómo utilizarlos.

Conductores (/api/v1/conductores/)
Método	Endpoint	Descripción
GET	/conductores/	Obtiene la lista de todos los conductores.
POST	/conductores/	Crea un nuevo conductor.
GET	/conductores/{id}/	Obtiene los detalles de un conductor específico.
PUT	/conductores/{id}/	Actualiza completamente un conductor.
DELETE	/conductores/{id}/	Elimina un conductor.

Ejemplos de uso con curl:
Crear un nuevo conductor:

Bash
curl -X POST http://127.0.0.1:8000/api/v1/conductores/ \
-H "Content-Type: application/json" \
-d '{
    "nombre": "Carlos Solis",
    "numero_licencia": "Y987654"
}'
Rutas (/api/v1/rutas/)

Método	Endpoint	Descripción
GET	/rutas/	Obtiene la lista de todas las rutas.
POST	/rutas/	Crea una nueva ruta y la asigna a un conductor.
GET	/rutas/{id}/	Obtiene los detalles de una ruta específica.
PUT	/rutas/{id}/	Actualiza completamente una ruta.
DELETE	/rutas/{id}/	Elimina una ruta.
GET	/rutas/?search=	Busca rutas por origen o destino.

Ejemplos de uso con curl:
Crear una nueva ruta (asumiendo que existe un conductor con id=1):

Bash
curl -X POST http://127.0.0.1:8000/api/v1/rutas/ \
-H "Content-Type: application/json" \
-d '{
    "origen": "Estadio Nacional",
    "destino": "Aeropuerto Jorge Chavez",
    "horario": "14:30:00",
    "conductor": 1
}'
Respuesta esperada (con el punto extra):

JSON
{
    "id": 1,
    "origen": "Estadio Nacional",
    "destino": "Aeropuerto Jorge Chavez",
    "horario": "14:30:00",
    "nombre_conductor": "Carlos Solis"
}

Buscar rutas cuyo origen o destino contenga "Aeropuerto":

Bash
curl -X GET http://127.0.0.1:8000/api/v1/rutas/?search=Aeropuerto