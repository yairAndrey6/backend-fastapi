# 🎬 Movies API - FastAPI

## 📌 Descripción
API REST desarrollada con **FastAPI** para la gestión de películas.  
Permite **listar, crear, actualizar y eliminar** registros de películas, con validaciones automáticas gracias a **Pydantic**.

---

## 🛠️ Tecnologías usadas
- Python 3.9+
- FastAPI
- Uvicorn
- Pydantic

---

## ⚙️ Instalación y configuración

1. **Clonar repositorio**
   ```bash
   git clone https://github.com/yairAndrey6/backend-fastapi.git
   cd backend-fastapi

2. **Instalar entorno virtual**
    ```bash
    python -m venv "nombre del entorno (preferencia puede ser venv)- >>sin comillas"

3. **Activar el entorno virtual**
    ```bash
    venv\Scripts\activate

4. **Instalar dependencias**
    ```bash
    pip install fastapi uvicorn

5. **Iniciar el servidor por un puerto en especifico**
    ```bash
    uvicorn main:app --reload --port "numero de puerto"


## Documentación automática
Swagger UI → http://127.0.0.1:numero_de_puerto/docs

## EndPoints principales
| Método | Endpoint       | Descripción                           |
| ------ | -------------- | ------------------------------------- |
| GET    | `/movies`      | Lista todas las películas             |
| GET    | `/movies/{id}` | Busca película por ID                 |
| POST   | `/movies`      | Agrega una nueva película             |
| PUT    | `/movies/{id}` | Actualiza información de una película |
| DELETE | `/movies/{id}` | Elimina una película                  |



