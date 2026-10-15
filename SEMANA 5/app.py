import streamlit as st
import supabase import Client, create_client

# key = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF4cmhvZXZmaHZ5b3Z0bnBtbHJrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTAxNjQzMzYsImV4cCI6MjEwNTc0MDMzNn0.XrzGMA2xYgIyA5rWERd75nEFMuUn37hlBH1Uak4ikyA

# url = https://axrhoevfhvyovtnpmlrk.supabase.co/rest/v1/

url: str = "https://axrhoevfhvyovtnpmlrk.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF4cmhvZXZmaHZ5b3Z0bnBtbHJrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTAxNjQzMzYsImV4cCI6MjEwNTc0MDMzNn0.XrzGMA2xYgIyA5rWERd75nEFMuUn37hlBH1Uak4ikyA"
supabase: Client = create_client(url, key)
# Codigo para testear la conexión a Supabase
#try:
#    test = supabase.table("datos").select("*").execute()
#    print("Conexión exitosa a Supabase", test.data)
# except Exception as e:
#    print("Error al conectar con Supabase:", e)

st.tittle("Crud con Supabase y Streamlit")
def get_datos():
    try:
        response = supabase.table("datos").select("*").execute()
        return response.data
    except Exception as e:
        st.error(f"Error al conectar con Supabase: {e}")
        return []

st.subheader("Lista de Registros en Supabase")

datos = get_datos()

if datos:
    datosfilas = pd.DataFrame(datos)

    st.dataframe(
        datosfilas,
        use_container_width=True,
        hide_index=True
        Column_order= ["id", "created_at", "nombre", "detalle", "estatus"]
        column_config={

        }
    )
    

