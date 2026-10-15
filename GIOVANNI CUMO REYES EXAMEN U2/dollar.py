from fastapi import FastAPI
import json
import uvicorn

app = FastAPI(
    title="API Histórico del Dólar 2026",
    description="API basada en el ejemplo de clase con datos del dólar.",
    version="1.0.0"
)

def cargar_base_datos():
    """Lee el archivo JSON y regresa la lista que está dentro de la llave 'Dolar'"""
    try:
        with open("dolar_historico.json", "r", encoding="utf-8") as f:
            contenido = json.load(f)
            return contenido.get("Dolar", [])
    except FileNotFoundError:
        return []

@app.get("/")
def data_info():
    return {
        "message": "Bienvenidos al API Histórico del Dólar 2026",
        "author": "Giovanni Cumo Reyes",
        "version": "1.0.0"
    }

# Endpoint para ver todos los registros
@app.get("/dolar")
def data_dolar():
    dolar_db = cargar_base_datos()
    return {
        "api_version": "v1",
        "total_records": len(dolar_db),
        "filters_applied": {
            "year": 2026
        },
        "data": dolar_db
    }

# Endpoint para buscar por fecha específica ajustado al estilo de tu compañero (sin raise)
@app.get("/dolar/{fecha}")
def consultar_fecha(fecha: str):
    dolar_db = cargar_base_datos()
    
    for registro in dolar_db:
        if registro["fecha"] == fecha:
            return registro

    return {"error": "No se encontró esa fecha en el historial."}

if __name__ == "__main__":
    uvicorn.run("dolar:app", host="127.0.0.1", port=8000, reload=True)