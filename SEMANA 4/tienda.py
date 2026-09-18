from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# ============================================================
# API EXTERNA
# ============================================================

API_EXTERNA = "https://fakestoreapi.com/products"

MARCAS = ["SprintMax", "StrideCo", "PumaFit"]

CATEGORIAS_MAP = {
    "men's clothing": "Ropa para hombre",
    "women's clothing": "Ropa para mujer",
    "jewelery": "Accesorios",
    "electronics": "Tecnología",
}


# ============================================================
# CARGAR PRODUCTOS
# ============================================================

def cargar_productos():
    productos = []

    try:
        respuesta = requests.get(API_EXTERNA, timeout=10)
        respuesta.raise_for_status()
        datos = respuesta.json()

        for i, item in enumerate(datos):
            categoria_original = item.get("category", "")
            categoria = CATEGORIAS_MAP.get(categoria_original, "Otros")

            producto = {
                "id": item.get("id"),
                "nombre": item.get("title"),
                "marca": MARCAS[i % len(MARCAS)],
                "categoria": categoria,
                "precio": item.get("price", 0),
                "descripcion": item.get("description", "Producto deportivo"),
                "color": "Variado",
                "stock": (i + 3) * 2,  # Fake Store no proporciona stock
                "imagen": item.get("image"),
                "rating": item.get("rating", {}).get("rate", 0),
                "opiniones": item.get("rating", {}).get("count", 0),
            }
            productos.append(producto)

        print(f"✓ Se cargaron {len(productos)} productos.")

    except Exception as e:
        print(f"❌ Error cargando productos: {e}")

    return productos


productos = cargar_productos()


# ============================================================
# INICIO
# ============================================================

@app.route("/")
def home():
    return jsonify({
        "mensaje": "Bienvenido a la API de SprintMax",
        "productos": len(productos)
    })


# ============================================================
# TODOS LOS PRODUCTOS
# ============================================================

@app.route("/productos", methods=["GET"])
def obtener_productos():
    return jsonify(productos)


# ============================================================
# PRODUCTO POR ID
# ============================================================

@app.route("/productos/<int:producto_id>", methods=["GET"])
def obtener_producto(producto_id):
    producto = next((p for p in productos if p["id"] == producto_id), None)

    if producto is None:
        return jsonify({"error": "Producto no encontrado"}), 404

    return jsonify(producto)


# ============================================================
# PRODUCTOS POR MARCA
# ============================================================

@app.route("/productos/marca/<string:marca>", methods=["GET"])
def obtener_por_marca(marca):
    resultado = [p for p in productos if p["marca"].lower() == marca.lower()]
    return jsonify(resultado)


# ============================================================
# PRODUCTOS POR CATEGORÍA
# ============================================================

@app.route("/productos/categoria/<string:categoria>", methods=["GET"])
def obtener_por_categoria(categoria):
    resultado = [p for p in productos if p["categoria"].lower() == categoria.lower()]
    return jsonify(resultado)


# ============================================================
# CATEGORÍAS
# ============================================================

@app.route("/categorias", methods=["GET"])
def obtener_categorias():
    categorias = sorted(set(p["categoria"] for p in productos))
    return jsonify(categorias)


# ============================================================
# RANGO DE PRECIOS (útil para el slider del front-end)
# ============================================================

@app.route("/precios/rango", methods=["GET"])
def obtener_rango_precios():
    if not productos:
        return jsonify({"min": 0, "max": 0})

    precios = [p["precio"] for p in productos]
    return jsonify({"min": min(precios), "max": max(precios)})


# ============================================================
# AGREGAR PRODUCTO
# ============================================================

@app.route("/productos", methods=["POST"])
def agregar_producto():
    nuevo = request.get_json()
    nuevo["id"] = max([p["id"] for p in productos], default=0) + 1
    productos.append(nuevo)
    return jsonify(nuevo), 201


# ============================================================
# EJECUTAR FLASK
# ============================================================

if __name__ == "__main__":
    app.run(debug=True, port=5000)