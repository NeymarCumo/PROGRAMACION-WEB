from datetime import date, timedelta
import json
import yfinance as yf

def crear_json_historico():
    print("Obteniendo datos del dólar para el JSON...")
    f_inicio = "2026-01-01"
    f_fin = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    
    df = yf.download("USDMXN=X", start=f_inicio, end=f_fin, progress=False)
    
    precios_reales = {}
    ultimo_precio = 17.50
    
    for fecha_idx, row in df.iterrows():
        f_obj = fecha_idx.date()
        precio = row["Close"]
        if hasattr(precio, "item"):
            precio = precio.item()
        ultimo_precio = float(precio)
        precios_reales[f_obj.strftime("%Y-%m-%d")] = round(ultimo_precio, 4)

    lista_dolar = []
    current_date = date(2026, 1, 1)
    fecha_limite = min(date.today(), date(2026, 12, 31))
    
    while current_date <= fecha_limite:
        iso_key = current_date.strftime("%Y-%m-%d")
        fecha_pizarron = current_date.strftime("%d-%m-%Y") # Formato "01-01-2026"
        
        if iso_key in precios_reales:
            precio_final = precios_reales[iso_key]
            ultimo_precio = precio_final
        else:
            precio_final = ultimo_precio

        lista_dolar.append({
            "fecha": fecha_pizarron,
            "precio": precio_final
        })
        current_date += timedelta(days=1)

    # Estructura exacta basada en la foto de tu JSON
    estructura_json = {
        "Dolar": lista_dolar
    }

    with open("dolar_historico.json", "w", encoding="utf-8") as f:
        json.dump(estructura_json, f, ensure_ascii=False, indent=4)
        
    print("¡Archivo 'dolar_historico.json' generado y vinculado exitosamente!")

if __name__ == "__main__":
    crear_json_historico()