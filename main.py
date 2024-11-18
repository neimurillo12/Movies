from fastapi import FastAPI,Query # Importamos la libreria FastAPI
from fastapi.responses import JSONResponse # Importamos la libreria JSONResponse
from fastapi.responses import HTMLResponse
from typing import Optional


app = FastAPI() #Crea una instancia de la clase FastAPI
app.title = "Pokedex"
app.version = "0.0.1"

movies_list = [
{
    "id": 1,
    "title": "Deadpool y Wolverine",
    "overviwe": "Deadpool se retira, pero regresa para salvar a sus seres queridos y al mundo, con la ayuda de Wolverine",
    "year": "2024",
    "rating": 8.5
},
{
    "id": 2,
    "title": "The Avengers",
    "overview": "Los vengadores se unen en una aventura peligrosa",
    "year": 2024,
    "rating": 9.5
},
{
    "id": 3,
    "title": "The Beast",
    "overview": "Cada una de esas épocas presenta distintas versiones de los personajes",
    "year": 2024,
    "rating": 6.5
},
{
    "id": 4,
    "title": "Inmaculada",
    "overview": "Maravillosa y espeluznante película de terror sobre una monja novicia",
    "year": 2024,
    "rating": 9.5
},
{
    "id": 5,
    "title": "Guerra Civil",
    "overview": "Una fibra sensible con su visión de un futuro cercano",
    "year": 2024,
    "rating": 5.5
},
{
    "id": 6,
    "title": "Love Lies Bleeding",
    "overview": "Una vida miserable al comienzo",
    "year": 2024,
    "rating": 3.5
},
{
    "id": 7,
    "title": "La Quimera",
    "overview": "Recorre la línea entre el realismo de ricas texturas y los sueños",
    "year": 2024,
    "rating": 8.5
},
{
    "id": 8,
    "title": "Mi Amigo Robot",
    "overview": "Un homenaje amoroso a la vitalidad de la Nueva York de los años 80",
    "year": 2024,
    "rating": 5.5
},
{
    "id": 9,
    "title": "Yo Capitán",
    "overview": "El traicionero viaje de un chico de 16 años",
    "year": 2024,
    "rating": 9.5
},
{
    "id": 10,
    "title": "Perfect Days",
    "overview": "encontró el secreto de la felicidad",
    "year": 2024,
    "rating": 1.5
}
 ]

@app.get('/', tags=["Home"]) #Definimos una ruta
def message(): # Definimos una función de la ruta
    return HTMLResponse ('<h1>Hola mundo<h1>') # Retorna un objeto de la clase HTMLResponse

@app.get('/movies', tags=["Movies"]) #Definimos una ruta de la clase FastAPI
def get_movies(): # aquí puse get_movies y estaba solo movies
    return movies_list

@app.get('/movies/{id}' , tags=["Movies"])
def get_movies(id: int):
    for item in movies_list:
        if item["id"] == id:
            return item
    return []