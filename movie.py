from pydantic import BaseModel, Field
from typing import Optional, List

# Creación del modelo de datos (esquema) (BaseModel) y validación de atributos que vienen por Body.
class Movie(BaseModel):
    id : Optional[int] = None
    year : int = Field(default=2023)
    descripcion : str = Field(default="Descripción de la película",min_length=5,max_length=80)
    autores : List[str] = Field(default=[], min_items=1, description="Debe tener al menos un autor")
    titulo : str = Field(default="Título de la película",min_length=5)
    ranking : float = Field(ge=1,le=10)
    categoria : str = Field(default="Categoría de la película",min_length=5,max_length=80)
