import streamlit as st
import random
import requests
import streamlit.components.v1 as components


# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Generador de Cartas Pokémon",
    page_icon="🃏",
    layout="centered"
)


# ============================================================
# ESTILO DE STREAMLIT
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at top,
            #ffffff 0%,
            #eef2f3 45%,
            #d7dde0 100%
        );
}

.titulo {
    text-align: center;
    font-size: 38px;
    font-weight: 900;
    color: #202020;
    margin-top: 20px;
    margin-bottom: 5px;
}

.subtitulo {
    text-align: center;
    font-size: 16px;
    color: #555;
    margin-bottom: 25px;
}

div[data-testid="stButton"] button {
    font-weight: bold;
    border-radius: 10px;
    height: 45px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# POKEAPI
# ============================================================

def get_pokemon_data(pokemon):

    try:

        pokemon = pokemon.lower().strip()

        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

        response = requests.get(
            url,
            timeout=10
        )

        if response.status_code == 200:

            return response.json()

        return None

    except requests.exceptions.RequestException as error:

        st.error(
            f"❌ Error al conectar con PokeAPI: {error}"
        )

        return None


# ============================================================
# POKÉMON ALEATORIO
# ============================================================

def get_random_pokemon():

    pokemon_id = random.randint(
        1,
        1025
    )

    return get_pokemon_data(
        str(pokemon_id)
    )


# ============================================================
# COLORES POR TIPO
# ============================================================

def get_type_color(pokemon_type):

    colors = {

        "normal": "#A8A77A",
        "fire": "#E85D04",
        "water": "#2774E8",
        "electric": "#E5B900",
        "grass": "#4FAE45",
        "ice": "#56C7D8",
        "fighting": "#B52B25",
        "poison": "#863A8C",
        "ground": "#B98A35",
        "flying": "#7868C9",
        "psychic": "#D63E70",
        "bug": "#789000",
        "rock": "#857326",
        "ghost": "#554080",
        "dragon": "#4E27C7",
        "dark": "#40342D",
        "steel": "#8585A5",
        "fairy": "#C76B9C"

    }

    return colors.get(
        pokemon_type,
        "#777777"
    )


# ============================================================
# FONDOS SEGÚN TIPO
# ============================================================

def get_type_background(pokemon_type):

    backgrounds = {

        "normal":
            "radial-gradient(circle, #f8f8f8, #c9c9b8 70%, #9e9e88)",

        "fire":
            "radial-gradient(circle, #ffd08a, #e85d04 45%, #7f1800)",

        "water":
            "radial-gradient(circle, #b9f3ff, #2774e8 45%, #09245c)",

        "electric":
            "radial-gradient(circle, #fff7a8, #e5b900 45%, #806600)",

        "grass":
            "radial-gradient(circle, #d6ffb5, #4fae45 45%, #164d19)",

        "ice":
            "radial-gradient(circle, #e5ffff, #56c7d8 45%, #236a78)",

        "fighting":
            "radial-gradient(circle, #ffb29c, #b52b25 45%, #55100c)",

        "poison":
            "radial-gradient(circle, #e7a5ef, #863a8c 45%, #351037)",

        "ground":
            "radial-gradient(circle, #f4d994, #b98a35 45%, #62430e)",

        "flying":
            "radial-gradient(circle, #e0dcff, #7868c9 45%, #332b66)",

        "psychic":
            "radial-gradient(circle, #ffc2d7, #d63e70 45%, #64152f)",

        "bug":
            "radial-gradient(circle, #e8f59a, #789000 45%, #354200)",

        "rock":
            "radial-gradient(circle, #eee1a2, #857326 45%, #403710)",

        "ghost":
            "radial-gradient(circle, #c4b3e8, #554080 45%, #211632)",

        "dragon":
            "radial-gradient(circle, #c8baff, #4e27c7 45%, #1a0a5c)",

        "dark":
            "radial-gradient(circle, #918477, #40342d 45%, #17120f)",

        "steel":
            "radial-gradient(circle, #e5e5ef, #8585a5 45%, #39394d)",

        "fairy":
            "radial-gradient(circle, #ffd5eb, #c76b9c 45%, #641d45)"

    }

    return backgrounds.get(
        pokemon_type,
        "radial-gradient(circle, #ffffff, #aaaaaa)"
    )


# ============================================================
# TIPOS EN ESPAÑOL
# ============================================================

def translate_type(pokemon_type):

    translations = {

        "normal": "Normal",
        "fire": "Fuego",
        "water": "Agua",
        "electric": "Eléctrico",
        "grass": "Planta",
        "ice": "Hielo",
        "fighting": "Lucha",
        "poison": "Veneno",
        "ground": "Tierra",
        "flying": "Volador",
        "psychic": "Psíquico",
        "bug": "Bicho",
        "rock": "Roca",
        "ghost": "Fantasma",
        "dragon": "Dragón",
        "dark": "Siniestro",
        "steel": "Acero",
        "fairy": "Hada"

    }

    return translations.get(
        pokemon_type,
        pokemon_type.capitalize()
    )


# ============================================================
# SÍMBOLOS
# ============================================================

def get_type_symbol(pokemon_type):

    symbols = {

        "normal": "★",
        "fire": "🔥",
        "water": "💧",
        "electric": "⚡",
        "grass": "🌿",
        "ice": "❄️",
        "fighting": "✊",
        "poison": "☠️",
        "ground": "◈",
        "flying": "🪽",
        "psychic": "🔮",
        "bug": "🪲",
        "rock": "◆",
        "ghost": "👻",
        "dragon": "🐉",
        "dark": "🌑",
        "steel": "⚙️",
        "fairy": "✨"

    }

    return symbols.get(
        pokemon_type,
        "★"
    )


# ============================================================
# DEBILIDADES
# ============================================================

def get_weakness(pokemon_type):

    weaknesses = {

        "normal": "Lucha",
        "fire": "Agua",
        "water": "Eléctrico",
        "electric": "Tierra",
        "grass": "Fuego",
        "ice": "Fuego",
        "fighting": "Volador",
        "poison": "Tierra",
        "ground": "Agua",
        "flying": "Eléctrico",
        "psychic": "Bicho",
        "bug": "Fuego",
        "rock": "Agua",
        "ghost": "Siniestro",
        "dragon": "Hielo",
        "dark": "Lucha",
        "steel": "Fuego",
        "fairy": "Acero"

    }

    return weaknesses.get(
        pokemon_type,
        "N/A"
    )


# ============================================================
# RESISTENCIAS
# ============================================================

def get_resistance(pokemon_type):

    resistances = {

        "normal": "—",
        "fire": "Planta",
        "water": "Fuego",
        "electric": "Acero",
        "grass": "Agua",
        "ice": "Hielo",
        "fighting": "Roca",
        "poison": "Planta",
        "ground": "Veneno",
        "flying": "Planta",
        "psychic": "Lucha",
        "bug": "Planta",
        "rock": "Normal",
        "ghost": "Veneno",
        "dragon": "Fuego",
        "dark": "Fantasma",
        "steel": "Acero",
        "fairy": "Siniestro"

    }

    return resistances.get(
        pokemon_type,
        "N/A"
    )


# ============================================================
# TÍTULO
# ============================================================

st.markdown(
    """
    <div class="titulo">
        🃏 Generador de Cartas Pokémon
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitulo">
        Busca un Pokémon o genera uno aleatoriamente utilizando PokeAPI.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# CONTROLES
# ============================================================

col1, col2 = st.columns(2)


with col1:

    pokemon_input = st.text_input(
        "🔎 Buscar Pokémon",
        placeholder="Ejemplo: pikachu"
    )


with col2:

    random_button = st.button(
        "🎲 Pokémon aleatorio",
        use_container_width=True
    )


# ============================================================
# OBTENER POKÉMON
# ============================================================

if random_button:

    data = get_random_pokemon()

elif pokemon_input:

    data = get_pokemon_data(
        pokemon_input
    )

else:

    data = get_pokemon_data(
        "pikachu"
    )


# ============================================================
# CARTA
# ============================================================

if data:

    # --------------------------------------------------------
    # DATOS
    # --------------------------------------------------------

    name = data["name"].capitalize()

    pokemon_id = data["id"]

    hp = data["stats"][0]["base_stat"]

    attack_stat = data["stats"][1]["base_stat"]

    defense_stat = data["stats"][2]["base_stat"]

    height = data["height"] / 10

    weight = data["weight"] / 10

    pokemon_type = data["types"][0]["type"]["name"]

    type_name = translate_type(
        pokemon_type
    )

    type_color = get_type_color(
        pokemon_type
    )

    type_background = get_type_background(
        pokemon_type
    )

    type_symbol = get_type_symbol(
        pokemon_type
    )

    weakness = get_weakness(
        pokemon_type
    )

    resistance = get_resistance(
        pokemon_type
    )


    # --------------------------------------------------------
    # IMAGEN
    # --------------------------------------------------------

    image_url = (
        data["sprites"]
        ["other"]
        ["official-artwork"]
        ["front_default"]
    )

    if not image_url:

        image_url = (
            data["sprites"]
            ["front_default"]
        )


    # --------------------------------------------------------
    # ATAQUE
    # --------------------------------------------------------

    if data["moves"]:

        attack_name = (
            data["moves"][0]["move"]["name"]
            .replace("-", " ")
            .title()
        )

    else:

        attack_name = "Ataque"


    # --------------------------------------------------------
    # DAÑO
    # --------------------------------------------------------

    damage = max(
        20,
        30 + (attack_stat // 4)
    )


    # ========================================================
    # HTML
    # ========================================================

    card_html = f"""

<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<style>

* {{
    box-sizing: border-box;
}}

body {{

    margin: 0;

    padding: 15px;

    background: transparent;

    font-family:
        Arial,
        Helvetica,
        sans-serif;

}}


/* ==========================================================
   CARTA
========================================================== */

.card {{

    width: 400px;

    height: 610px;

    margin: auto;

    padding: 13px;

    position: relative;

    overflow: hidden;

    border-radius: 25px;

    border:
        8px solid {type_color};

    background:
        linear-gradient(
            145deg,
            #ffffff,
            #eeeeee
        );

    box-shadow:

        0 4px 8px
        rgba(0,0,0,0.25),

        0 18px 35px
        rgba(0,0,0,0.30);

}}


/* ==========================================================
   BRILLO HOLOGRÁFICO
========================================================== */

.card::before {{

    content: "";

    position: absolute;

    inset: -100%;

    background:
        linear-gradient(
            120deg,
            transparent 35%,
            rgba(255,255,255,0.65) 45%,
            rgba(255,255,255,0.15) 50%,
            transparent 60%
        );

    transform:
        rotate(20deg);

    animation:
        holo 5s infinite linear;

    pointer-events: none;

    z-index: 10;

}}

@keyframes holo {{

    0% {{
        transform:
            translateX(-50%)
            rotate(20deg);
    }}

    100% {{
        transform:
            translateX(50%)
            rotate(20deg);
    }}

}}


/* ==========================================================
   DESTELLOS
========================================================== */

.sparkle {{

    position: absolute;

    color: white;

    font-size: 17px;

    text-shadow:
        0 0 8px white;

    z-index: 20;

    pointer-events: none;

}}

.sparkle.one {{
    top: 105px;
    left: 35px;
}}

.sparkle.two {{
    top: 190px;
    right: 30px;
}}

.sparkle.three {{
    top: 280px;
    left: 48px;
}}


/* ==========================================================
   CABECERA
========================================================== */

.header {{

    height: 43px;

    display: flex;

    align-items: center;

    gap: 8px;

    position: relative;

    z-index: 30;

}}

.basic {{

    font-size: 11px;

    font-weight: bold;

    color: #333;

}}

.name {{

    flex: 1;

    font-size: 26px;

    font-weight: 900;

    color: #202020;

    white-space: nowrap;

    overflow: hidden;

    text-overflow: ellipsis;

}}

.hp {{

    font-size: 19px;

    font-weight: 900;

    color: #202020;

    white-space: nowrap;

}}


/* ==========================================================
   ZONA DE IMAGEN
========================================================== */

.image-container {{

    height: 275px;

    width: 100%;

    position: relative;

    overflow: hidden;

    border-radius: 8px;

    border:
        4px solid {type_color};

    background:
        {type_background};

    box-shadow:

        inset 0 0 25px
        rgba(0,0,0,0.35),

        0 2px 4px
        rgba(0,0,0,0.25);

}}


/* LUZ DEL FONDO */

.image-container::after {{

    content: "";

    position: absolute;

    inset: 0;

    background:
        radial-gradient(
            circle at 50% 40%,
            rgba(255,255,255,0.45),
            transparent 48%
        );

    pointer-events: none;

}}


/* ==========================================================
   IMAGEN DEL POKÉMON
========================================================== */

.pokemon-image {{

    position: relative;

    z-index: 5;

    width: 270px;

    height: 270px;

    display: block;

    margin: auto;

    object-fit: contain;

    filter:

        drop-shadow(
            0 10px 6px
            rgba(0,0,0,0.40)
        );

}}


/* ==========================================================
   INFORMACIÓN
========================================================== */

.info {{

    height: 29px;

    margin-top: 7px;

    display: flex;

    align-items: center;

    justify-content: center;

    gap: 8px;

    border:
        2px solid #777;

    background:
        linear-gradient(
            #eeeeee,
            #cccccc
        );

    font-size: 10px;

    font-weight: bold;

    color: #333;

}}


/* ==========================================================
   TIPO
========================================================== */

.type-section {{

    text-align: center;

    margin-top: 8px;

}}

.type-title {{

    font-size: 14px;

    font-weight: 900;

}}

.type-badge {{

    display: inline-block;

    margin-top: 3px;

    padding:
        4px 12px;

    border-radius: 15px;

    background:
        {type_color};

    color: white;

    font-size: 9px;

    font-weight: bold;

    box-shadow:
        0 2px 4px
        rgba(0,0,0,0.25);

}}


/* ==========================================================
   ATAQUE
========================================================== */

.attack {{

    margin-top: 9px;

    padding:
        7px 6px;

    border-top:
        2px solid #777;

    border-bottom:
        2px solid #777;

}}

.attack-row {{

    display: flex;

    align-items: center;

    justify-content: space-between;

}}

.attack-name {{

    font-size: 17px;

    font-weight: 900;

    color: #222;

}}

.damage {{

    font-size: 23px;

    font-weight: 900;

    color: #222;

}}

.attack-description {{

    margin-left: 28px;

    margin-top: 3px;

    font-size: 9px;

    color: #444;

}}


/* ==========================================================
   INFORMACIÓN INFERIOR
========================================================== */

.footer {{

    display: grid;

    grid-template-columns:
        1fr 1fr 1fr;

    margin-top: 9px;

    padding-top: 6px;

    border-top:
        2px solid #777;

    text-align: center;

}}

.footer-item {{

    border-right:
        1px solid #aaa;

}}

.footer-item:last-child {{

    border-right: none;

}}

.footer-title {{

    font-size: 8px;

    font-weight: bold;

}}

.footer-value {{

    font-size: 9px;

    margin-top: 3px;

}}


/* ==========================================================
   NÚMERO
========================================================== */

.number {{

    position: absolute;

    right: 17px;

    bottom: 8px;

    font-size: 8px;

    color: #555;

}}


/* ==========================================================
   RAREZA
========================================================== */

.rarity {{

    position: absolute;

    left: 17px;

    bottom: 7px;

    font-size: 12px;

    color: #555;

}}

</style>

</head>


<body>


<div class="card">


    <!-- DESTELLOS -->

    <div class="sparkle one">✦</div>

    <div class="sparkle two">✦</div>

    <div class="sparkle three">✧</div>


    <!-- ==================================================
         CABECERA
    =================================================== -->

    <div class="header">

        <div class="basic">

            Básico

        </div>


        <div class="name">

            {name}

        </div>


        <div class="hp">

            HP {hp}

        </div>

    </div>


    <!-- ==================================================
         IMAGEN
    =================================================== -->

    <div
        class="image-container"
    >

        <img
            class="pokemon-image"
            src="{image_url}"
            alt="{name}"
        >

    </div>


    <!-- ==================================================
         INFORMACIÓN
    =================================================== -->

    <div class="info">

        <span>
            No. {pokemon_id:03d}
        </span>

        <span>•</span>

        <span>
            Altura {height:.1f} m
        </span>

        <span>•</span>

        <span>
            Peso {weight:.1f} kg
        </span>

    </div>


    <!-- ==================================================
         TIPO
    =================================================== -->

    <div class="type-section">

        <div class="type-title">

            {type_symbol}
            Pokémon {type_name}

        </div>


        <div class="type-badge">

            {type_name.upper()}

        </div>

    </div>


    <!-- ==================================================
         ATAQUE
    =================================================== -->

    <div class="attack">

        <div class="attack-row">

            <div class="attack-name">

                {type_symbol}
                {attack_name}

            </div>


            <div class="damage">

                {damage}

            </div>

        </div>


        <div class="attack-description">

            Un poderoso ataque de tipo
            {type_name}.

        </div>

    </div>


    <!-- ==================================================
         PIE
    =================================================== -->

    <div class="footer">


        <div class="footer-item">

            <div class="footer-title">

                DEBILIDAD

            </div>

            <div class="footer-value">

                {weakness} ×2

            </div>

        </div>


        <div class="footer-item">

            <div class="footer-title">

                RESISTENCIA

            </div>

            <div class="footer-value">

                {resistance}

            </div>

        </div>


        <div class="footer-item">

            <div class="footer-title">

                DEFENSA

            </div>

            <div class="footer-value">

                {defense_stat}

            </div>

        </div>


    </div>


    <!-- RAREZA -->

    <div class="rarity">

        ◆ RARA

    </div>


    <!-- NÚMERO -->

    <div class="number">

        #{pokemon_id:03d}

    </div>


</div>


</body>

</html>

"""


    # ========================================================
    # MOSTRAR CARTA
    # ========================================================

    components.html(
        card_html,
        height=650,
        scrolling=False
    )


else:

    st.error(
        "❌ No se encontró el Pokémon. "
        "Revisa el nombre e inténtalo nuevamente."
    )