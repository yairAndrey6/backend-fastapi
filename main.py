from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from movie import Movie 


app = FastAPI(
    title="Aprendiendo FastAPI",
    description="API",
    version="1.0",
)
movies = [
    {
        "id": 1,
        "año": 2000,
        "descripcion": "Un hacker descubre la verdad detrás de su mundo simulado.",
        "autores": ["Lana Wachowski", "Lilly Wachowski"],
        "titulo": "The Matrix",
        "ranking": 9.0,
        "categoria": "Ciencia Ficción"
    },
    {
        "id": 2,
        "año": 2008,
        "descripcion": "Un multimillonario crea un traje de alta tecnología para convertirse en superhéroe.",
        "autores": ["Jon Favreau"],
        "titulo": "Iron Man",
        "ranking": 8.5,
        "categoria": "Acción"
    },
    {
        "id": 3,
        "año": 2014,
        "descripcion": "Un grupo de héroes intergalácticos debe salvar el universo de un villano poderoso.",
        "autores": ["James Gunn"],
        "titulo": "Guardians of the Galaxy",
        "ranking": 8.0,
        "categoria": "Aventura"
    }
]


# Página principal
@app.get("/", tags=["Endpoint Inicio"])
def read_root():
    return HTMLResponse("<h2>Hola mundo!</h2>")


# Obtener todas las movies
@app.get("/movies/", tags=["Endpoints Movies"])
def get_movies():
    return JSONResponse(content=movies)


# Obtener movie por id. Enviado por param
@app.get("/movies/id/{id}", tags=["Endpoints Movies"])
def get_movie_by_id(id:int = Path(ge=1,le=10)):
    for item in movies:
        if item["id"] == id:
            return item 
    return "Información con ese id no se encuentra"


# Obtener movie por año
@app.get("/movies/year/{year}", tags=["Endpoints Movies"])
def get_movie_by_year(year:int = Path(ge=2000,le=2025)):
    for item in movies:
        if item["año"] == year:
            return item 
    return "Película con ese año no se encuentra"


# Obtener movie por categoría (Pasado por Query). Validación de datos por Query
@app.get("/movies/category",tags=["Endpoints Movies"])
def get_movie_by_category(category:str = Query(min_length=5,max_length=80)):
    for item in movies:
        print(item)
        if item["categoria"] == category:
            return item
    return "Movie not Found"


# Agregar una película 
@app.post("/movies/add_movie/", tags=["Endpoints Movies"],status_code=201)
def create_movie(movie:Movie): 
    try:
        movies.append(movie)
        print(movies)
        return JSONResponse(content={"message": "Movie Added", "movie":[movie.dict() for m in movies]}) 
    except Exception as e:print("Error ", e)


# Actualizar movie por id
@app.put("/movies/{id}",tags=["Endpoints Movies"])
def update_movie(id:int, movie:Movie):
    try:
        for item in movies:
            if item["id"] == id:
                item["año"] = movie.year
                item["descripcion"] = movie.descripcion
                item["autores"] = movie.autores
                item["titulo"] = movie.titulo
                item["ranking"] = movie.ranking
                item["categoria"] = movie.categoria
                return JSONResponse(content={"message": "Movie Updated"})
    except Exception as e: print("Error: ", e)

# Eliminar movie por id
@app.delete("/movies/delete_by_id/{id}", tags=["Endpoints Movies"],status_code=200)
def delete_movie(id:int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            print(movies)
            return JSONResponse(content={"message": "Movie Deleted"})