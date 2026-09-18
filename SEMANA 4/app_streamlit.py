import math

import requests
import streamlit as st

# ============================================================
# CONFIGURACIÓN
# ============================================================

API_URL = "http://127.0.0.1:5000"
PRODUCTOS_POR_PAGINA = 6

st.set_page_config(
    page_title="SprintMax",
    page_icon="👟",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# ESTADO
# ============================================================

if "pagina" not in st.session_state:
    st.session_state.pagina = 1

if "carrito" not in st.session_state:
    st.session_state.carrito = {}  # id_producto -> cantidad

if "mostrar_carrito" not in st.session_state:
    st.session_state.mostrar_carrito = False


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
<style>

    .stApp {
        background: #ffffff;
    }

    .block-container {
        max-width: 1300px;
        padding-top: 1.2rem;
        padding-bottom: 3rem;
    }

    #MainMenu, footer, header {
        visibility: hidden;
    }

    h1, h2, h3, h4, p, span, div {
        color: #111111;
    }

    /* ---------- Logo ---------- */
    .logo {
        font-size: 26px;
        font-weight: 900;
        letter-spacing: 1px;
        padding-top: 6px;
    }

    /* ---------- Canasta ---------- */
    .cart-pill {
        text-align: right;
        font-weight: 700;
        font-size: 15px;
        padding-top: 12px;
        color: #333333;
    }

    /* ---------- Info de página ---------- */
    .pagina-info {
        text-align: center;
        font-weight: 700;
        font-size: 15px;
        color: #333333;
        margin: 18px 0 14px 0;
    }

    /* ---------- Badge de categoría ---------- */
    .badge {
        display: inline-block;
        background: #fbe6e6;
        color: #c0392b;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 0.4px;
        padding: 4px 10px;
        border-radius: 4px;
        margin-bottom: 8px;
    }

    /* ---------- Textos de producto ---------- */
    .product-name {
        font-size: 14px;
        font-weight: 700;
        color: #111111;
        min-height: 40px;
        line-height: 1.3;
    }

    .product-price {
        font-size: 18px;
        font-weight: 900;
        color: #00a896;
        margin-top: 4px;
    }

    .product-stock {
        font-size: 12px;
        color: #6a6a6a;
        margin-top: 2px;
    }

    /* ---------- Separador suave ---------- */
    .linea-suave {
        height: 1px;
        background: #eaeaea;
        margin: 6px 0 20px 0;
    }

    /* ---------- Footer claro ---------- */
    .footer-claro {
        text-align: center;
        color: #888888;
        font-size: 13px;
        padding: 30px 0 10px 0;
        margin-top: 40px;
        border-top: 1px solid #eaeaea;
    }

    /* Botones: fondo oscuro con texto blanco, legible siempre */
    .stButton > button {
        background-color: #111111 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 6px;
        font-weight: 700;
        font-size: 13px;
    }

    .stButton > button p,
    .stButton > button span,
    .stButton > button div {
        color: #ffffff !important;
    }

    .stButton > button:hover {
        background-color: #333333 !important;
        color: #ffffff !important;
    }

    .stButton > button:disabled {
        background-color: #cccccc !important;
        color: #888888 !important;
    }

    /* ---------- Imágenes de producto: tamaño parejo y contenido ---------- */
    div[data-testid="stImage"] {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 190px;
        overflow: hidden;
        margin-bottom: 6px;
    }

    div[data-testid="stImage"] img {
        height: 100% !important;
        width: 100% !important;
        object-fit: contain !important;
    }

    /* ---------- Forzar tema claro en buscador, selects y sliders ---------- */
    .stTextInput input {
        background-color: #ffffff !important;
        color: #111111 !important;
        border: 1px solid #dddddd !important;
        border-radius: 6px !important;
    }

    .stTextInput input::placeholder {
        color: #999999 !important;
    }

    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #111111 !important;
        border: 1px solid #dddddd !important;
        border-radius: 6px !important;
    }

    div[data-baseweb="select"] span {
        color: #111111 !important;
    }

    /* El menú desplegable se renderiza en un portal aparte */
    div[data-baseweb="popover"],
    div[data-baseweb="popover"] * {
        background-color: #ffffff !important;
        color: #111111 !important;
    }

    div[data-baseweb="popover"] {
        border: 1px solid #dddddd !important;
    }

    li[role="option"]:hover,
    li[aria-selected="true"] {
        background-color: #f4f4f4 !important;
        color: #111111 !important;
    }

    /* El popover de "Detalles" reutiliza los botones normales dentro,
       así que sus botones internos deben verse como los demás */
    div[data-baseweb="popover"] .stButton > button,
    div[data-baseweb="popover"] .stButton > button * {
        background-color: #111111 !important;
        color: #ffffff !important;
    }

    .stSlider label,
    .stSlider [data-testid="stTickBarMin"],
    .stSlider [data-testid="stTickBarMax"],
    .stSlider div[data-testid="stThumbValue"] {
        color: #111111 !important;
    }

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# CONECTAR CON FLASK
# ============================================================

try:
    respuesta = requests.get(f"{API_URL}/productos", timeout=10)
    respuesta.raise_for_status()
    productos = respuesta.json()

except Exception:
    st.error("❌ No se pudo conectar con Flask.")
    st.warning("Ejecuta primero: python tienda.py")
    st.stop()

if not productos:
    st.warning("No hay productos disponibles todavía.")
    st.stop()


# ============================================================
# ENCABEZADO
# ============================================================

col_logo, col_cart = st.columns([4, 1])

with col_logo:
    st.markdown('<div class="logo">SPRINTMAX</div>', unsafe_allow_html=True)

with col_cart:
    total_items = sum(st.session_state.carrito.values())
    if st.button(f"🛒 Ver Canasta ({total_items})", use_container_width=True):
        st.session_state.mostrar_carrito = not st.session_state.mostrar_carrito

st.markdown('<div class="linea-suave"></div>', unsafe_allow_html=True)


# ============================================================
# CANASTA (desplegable)
# ============================================================

if st.session_state.mostrar_carrito:
    with st.container(border=True):
        if not st.session_state.carrito:
            st.write("Tu canasta está vacía.")
        else:
            id_a_producto = {p["id"]: p for p in productos}
            subtotal = 0.0

            for pid, cantidad in st.session_state.carrito.items():
                prod = id_a_producto.get(pid)
                if not prod:
                    continue
                importe = prod["precio"] * cantidad
                subtotal += importe

                c1, c2, c3, c4 = st.columns([4, 1, 2, 1])
                with c1:
                    st.write(prod["nombre"])
                with c2:
                    st.write(f"x{cantidad}")
                with c3:
                    st.write(f"${importe:.2f} USD")
                with c4:
                    if st.button("Quitar", key=f"quitar_{pid}"):
                        del st.session_state.carrito[pid]
                        st.rerun()

            st.markdown(f"**Subtotal: ${subtotal:.2f} USD**")


# ============================================================
# BARRA DE FILTROS
# ============================================================

f1, f2, f3 = st.columns([2, 1, 2])

with f1:
    busqueda = st.text_input(
        "Buscar",
        placeholder="Ej. Mochila, Playera...",
        label_visibility="collapsed",
    )

with f2:
    categorias = ["Todas las categorías"] + sorted(
        set(p["categoria"] for p in productos)
    )
    categoria_sel = st.selectbox(
        "Categoría", categorias, label_visibility="collapsed"
    )

with f3:
    precios = [p["precio"] for p in productos]
    precio_min, precio_max = float(min(precios)), float(max(precios))

    if precio_min == precio_max:
        precio_max += 1.0

    rango_precio = st.slider(
        "Precio",
        min_value=precio_min,
        max_value=precio_max,
        value=(precio_min, precio_max),
        label_visibility="collapsed",
    )

st.markdown('<div class="linea-suave"></div>', unsafe_allow_html=True)


# ============================================================
# APLICAR FILTROS
# ============================================================

resultado = productos

if busqueda:
    resultado = [p for p in resultado if busqueda.lower() in p["nombre"].lower()]

if categoria_sel != "Todas las categorías":
    resultado = [p for p in resultado if p["categoria"] == categoria_sel]

resultado = [
    p for p in resultado if rango_precio[0] <= p["precio"] <= rango_precio[1]
]


# ============================================================
# PAGINACIÓN
# ============================================================

total_productos = len(resultado)
total_paginas = max(1, math.ceil(total_productos / PRODUCTOS_POR_PAGINA))

if st.session_state.pagina > total_paginas:
    st.session_state.pagina = 1

st.markdown(
    f'<div class="pagina-info">'
    f"Página {st.session_state.pagina} de {total_paginas} "
    f"({total_productos} productos)"
    f"</div>",
    unsafe_allow_html=True,
)

nav1, nav2, nav3 = st.columns([1, 6, 1])

with nav1:
    if st.button("⬅ Anterior", disabled=st.session_state.pagina <= 1):
        st.session_state.pagina -= 1
        st.rerun()

with nav3:
    if st.button(
        "Siguiente ➡", disabled=st.session_state.pagina >= total_paginas
    ):
        st.session_state.pagina += 1
        st.rerun()

inicio = (st.session_state.pagina - 1) * PRODUCTOS_POR_PAGINA
fin = inicio + PRODUCTOS_POR_PAGINA
productos_pagina = resultado[inicio:fin]


# ============================================================
# GRID DE PRODUCTOS
# ============================================================

if not productos_pagina:
    st.info("No se encontraron productos con estos filtros.")
else:
    filas = math.ceil(len(productos_pagina) / 3)
    idx = 0

    for _ in range(filas):
        columnas = st.columns(3)

        for columna in columnas:
            if idx >= len(productos_pagina):
                break

            producto = productos_pagina[idx]
            idx += 1

            with columna:
                with st.container(border=True):
                    st.image(producto["imagen"], use_container_width=True)

                    st.markdown(
                        f'<div class="badge">{producto["categoria"].upper()}</div>',
                        unsafe_allow_html=True,
                    )

                    st.markdown(
                        f'<div class="product-name">{producto["nombre"]}</div>',
                        unsafe_allow_html=True,
                    )

                    st.markdown(
                        f'<div class="product-price">${producto["precio"]:.2f} USD</div>',
                        unsafe_allow_html=True,
                    )

                    st.markdown(
                        f'<div class="product-stock">✓ En stock ({producto["stock"]})</div>',
                        unsafe_allow_html=True,
                    )

                    b1, b2 = st.columns(2)

                    with b1:
                        if st.button(
                            "Agregar", key=f"agregar_{producto['id']}",
                            use_container_width=True,
                        ):
                            st.session_state.carrito[producto["id"]] = (
                                st.session_state.carrito.get(producto["id"], 0) + 1
                            )
                            st.rerun()

                    with b2:
                        with st.popover("Detalles", use_container_width=True):
                            st.write(producto["descripcion"])
                            st.write(f"**Marca:** {producto['marca']}")
                            if producto.get("opiniones"):
                                st.write(
                                    f"⭐ {producto['rating']} "
                                    f"({producto['opiniones']} opiniones)"
                                )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer-claro">
        SPRINTMAX · Tienda deportiva · Desarrollado con Flask + Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)