from fastapi import FastAPI, HTTPException

app = FastAPI()

peliculas = [
    {"id": 1, "titulo": "The Shawshank Redemption", "director": "Frank Darabont", "anio": 1994, "genero": "Drama", "calificacion": 9.3},
    {"id": 2, "titulo": "The Godfather", "director": "Francis Ford Coppola", "anio": 1972, "genero": "Crimen", "calificacion": 9.2},
    {"id": 3, "titulo": "The Dark Knight", "director": "Christopher Nolan", "anio": 2008, "genero": "Acción", "calificacion": 9.0},
    {"id": 4, "titulo": "Pulp Fiction", "director": "Quentin Tarantino", "anio": 1994, "genero": "Crimen", "calificacion": 8.9},
    {"id": 5, "titulo": "Forrest Gump", "director": "Robert Zemeckis", "anio": 1994, "genero": "Drama", "calificacion": 8.8},
    {"id": 6, "titulo": "Inception", "director": "Christopher Nolan", "anio": 2010, "genero": "Ciencia ficción", "calificacion": 8.8},
    {"id": 7, "titulo": "Fight Club", "director": "David Fincher", "anio": 1999, "genero": "Drama", "calificacion": 8.8},
    {"id": 8, "titulo": "The Matrix", "director": "Lana y Lilly Wachowski", "anio": 1999, "genero": "Ciencia ficción", "calificacion": 8.7},
    {"id": 9, "titulo": "Goodfellas", "director": "Martin Scorsese", "anio": 1990, "genero": "Crimen", "calificacion": 8.7},
    {"id": 10, "titulo": "Interstellar", "director": "Christopher Nolan", "anio": 2014, "genero": "Ciencia ficción", "calificacion": 8.7},
    {"id": 11, "titulo": "Parasite", "director": "Bong Joon-ho", "anio": 2019, "genero": "Thriller", "calificacion": 8.5},
    {"id": 12, "titulo": "Gladiator", "director": "Ridley Scott", "anio": 2000, "genero": "Acción", "calificacion": 8.5},
    {"id": 13, "titulo": "The Lion King", "director": "Roger Allers y Rob Minkoff", "anio": 1994, "genero": "Animación", "calificacion": 8.5},
    {"id": 14, "titulo": "Titanic", "director": "James Cameron", "anio": 1997, "genero": "Romance", "calificacion": 7.9},
    {"id": 15, "titulo": "Jurassic Park", "director": "Steven Spielberg", "anio": 1993, "genero": "Aventura", "calificacion": 8.2},
    {"id": 16, "titulo": "Schindler's List", "director": "Steven Spielberg", "anio": 1993, "genero": "Drama", "calificacion": 9.0},
    {"id": 17, "titulo": "Star Wars: Episodio IV - Una nueva esperanza", "director": "George Lucas", "anio": 1977, "genero": "Ciencia ficción", "calificacion": 8.6},
    {"id": 18, "titulo": "The Silence of the Lambs", "director": "Jonathan Demme", "anio": 1991, "genero": "Thriller", "calificacion": 8.6},
    {"id": 19, "titulo": "Saving Private Ryan", "director": "Steven Spielberg", "anio": 1998, "genero": "Bélico", "calificacion": 8.6},
    {"id": 20, "titulo": "Back to the Future", "director": "Robert Zemeckis", "anio": 1985, "genero": "Ciencia ficción", "calificacion": 8.5},
    {"id": 21, "titulo": "Spirited Away", "director": "Hayao Miyazaki", "anio": 2001, "genero": "Animación", "calificacion": 8.6},
    {"id": 22, "titulo": "Toy Story", "director": "John Lasseter", "anio": 1995, "genero": "Animación", "calificacion": 8.3},
    {"id": 23, "titulo": "The Lord of the Rings: The Fellowship of the Ring", "director": "Peter Jackson", "anio": 2001, "genero": "Fantasía", "calificacion": 8.9},
    {"id": 24, "titulo": "Se7en", "director": "David Fincher", "anio": 1995, "genero": "Thriller", "calificacion": 8.6},
    {"id": 25, "titulo": "Terminator 2: Judgment Day", "director": "James Cameron", "anio": 1991, "genero": "Acción", "calificacion": 8.6},
    {"id": 26, "titulo": "Alien", "director": "Ridley Scott", "anio": 1979, "genero": "Terror", "calificacion": 8.5},
    {"id": 27, "titulo": "Casablanca", "director": "Michael Curtiz", "anio": 1942, "genero": "Romance", "calificacion": 8.5},
    {"id": 28, "titulo": "Psycho", "director": "Alfred Hitchcock", "anio": 1960, "genero": "Terror", "calificacion": 8.5},
    {"id": 29, "titulo": "The Departed", "director": "Martin Scorsese", "anio": 2006, "genero": "Crimen", "calificacion": 8.5},
    {"id": 30, "titulo": "Whiplash", "director": "Damien Chazelle", "anio": 2014, "genero": "Drama", "calificacion": 8.5},
    {"id": 31, "titulo": "Coco", "director": "Lee Unkrich", "anio": 2017, "genero": "Animación", "calificacion": 8.4},
    {"id": 32, "titulo": "Avengers: Endgame", "director": "Anthony y Joe Russo", "anio": 2019, "genero": "Acción", "calificacion": 8.4},
    {"id": 33, "titulo": "Mad Max: Fury Road", "director": "George Miller", "anio": 2015, "genero": "Acción", "calificacion": 8.1},
    {"id": 34, "titulo": "La La Land", "director": "Damien Chazelle", "anio": 2016, "genero": "Musical", "calificacion": 8.0},
    {"id": 35, "titulo": "Joker", "director": "Todd Phillips", "anio": 2019, "genero": "Drama", "calificacion": 8.4},
    {"id": 36, "titulo": "Django Unchained", "director": "Quentin Tarantino", "anio": 2012, "genero": "Western", "calificacion": 8.5},
    {"id": 37, "titulo": "The Prestige", "director": "Christopher Nolan", "anio": 2006, "genero": "Misterio", "calificacion": 8.5},
    {"id": 38, "titulo": "Amélie", "director": "Jean-Pierre Jeunet", "anio": 2001, "genero": "Comedia", "calificacion": 8.3},
    {"id": 39, "titulo": "El laberinto del fauno", "director": "Guillermo del Toro", "anio": 2006, "genero": "Fantasía", "calificacion": 8.2},
    {"id": 40, "titulo": "Gravity", "director": "Alfonso Cuarón", "anio": 2013, "genero": "Ciencia ficción", "calificacion": 7.7},
    {"id": 41, "titulo": "Roma", "director": "Alfonso Cuarón", "anio": 2018, "genero": "Drama", "calificacion": 7.7},
    {"id": 42, "titulo": "Amores perros", "director": "Alejandro González Iñárritu", "anio": 2000, "genero": "Drama", "calificacion": 8.0},
    {"id": 43, "titulo": "The Revenant", "director": "Alejandro González Iñárritu", "anio": 2015, "genero": "Aventura", "calificacion": 8.0},
    {"id": 44, "titulo": "Blade Runner", "director": "Ridley Scott", "anio": 1982, "genero": "Ciencia ficción", "calificacion": 8.1},
    {"id": 45, "titulo": "Scarface", "director": "Brian De Palma", "anio": 1983, "genero": "Crimen", "calificacion": 8.3},
    {"id": 46, "titulo": "Apocalypse Now", "director": "Francis Ford Coppola", "anio": 1979, "genero": "Bélico", "calificacion": 8.4},
    {"id": 47, "titulo": "The Shining", "director": "Stanley Kubrick", "anio": 1980, "genero": "Terror", "calificacion": 8.4},
    {"id": 48, "titulo": "2001: A Space Odyssey", "director": "Stanley Kubrick", "anio": 1968, "genero": "Ciencia ficción", "calificacion": 8.3},
    {"id": 49, "titulo": "Oppenheimer", "director": "Christopher Nolan", "anio": 2023, "genero": "Drama", "calificacion": 8.3},
    {"id": 50, "titulo": "Everything Everywhere All at Once", "director": "Daniel Kwan y Daniel Scheinert", "anio": 2022, "genero": "Ciencia ficción", "calificacion": 7.8},
]


@app.get("/")
def data_info():
    return {
        "message": "Bienvenidos a este ejemplo de API con FastAPI",
        "author": "Giovanni Cumo Reyes",
        "version": "1.0.0"
    }


@app.get("/peliculas")
def listar_peliculas():
    return peliculas


@app.get("/peliculas/{pelicula_id}")
def obtener_pelicula(pelicula_id: int):
    for p in peliculas:
        if p["id"] == pelicula_id:
            return p
    raise HTTPException(status_code=404, detail="Película no encontrada")