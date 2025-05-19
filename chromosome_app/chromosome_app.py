import streamlit as st
import pandas as pd
from PIL import Image
import os

# Configuración de la página
st.set_page_config(page_title="Visualizador de Cromosomas", page_icon="🧬")

st.title("🧬 Visualizador de Cromosomas Humanos")

# Carga de datos
@st.cache_data
def cargar_datos():
    data = {
        'Cromosoma': [1, 2, 3, 'X', 'Y'],
        'Descripción': [
            "Cromosoma más grande del genoma humano",
            "Involucrado en desarrollo y neurobiología",
            "Contiene genes implicados en cáncer renal",
            "Determina características sexuales femeninas",
            "Pequeño, con pocos genes funcionales"
        ],
        'Número de genes': [2058, 1293, 1052, 850, 60],
        'Sitios frágiles': [5, 3, 2, 4, 1],
        'Pseudogenes': [324, 198, 156, 232, 45],
        'Sondas': [12, 9, 7, 10, 3],
        'G. asociados a cáncer>1': ["BRCA1", "MYCN", "VHL", "FOXP3", "SRY"],
        '1p36': ["1p36 deletion syndrome", "", "", "", ""],
        'Sí2': ["Sí", "No", "", "Sí", "Sí"]
    }
    return pd.DataFrame(data)

df = cargar_datos()

# Selector de cromosoma
cromosoma = st.selectbox("Selecciona un cromosoma", df["Cromosoma"].unique())

# Filtrar datos
datos_cromo = df[df["Cromosoma"] == cromosoma].iloc[0]

# Mostrar información
st.subheader(f"📊 Información del Cromosoma {cromosoma}")

col1, col2 = st.columns(2)

with col1:
    st.metric("Número de genes", datos_cromo["Número de genes"])
    st.metric("Sitios frágiles", datos_cromo["Sitios frágiles"])
    st.metric("Pseudogenes", datos_cromo["Pseudogenes"])

with col2:
    st.metric("Sondas", datos_cromo["Sondas"])
    st.metric("Genes cáncer", datos_cromo["G. asociados a cáncer>1"])
    st.metric("Síndromes", datos_cromo["1p36"] if datos_cromo["1p36"] else "No especificado")

# Mostrar descripción
st.subheader("Descripción")
st.write(datos_cromo["Descripción"])

# Manejo de imágenes (opcional)
ruta_imagen = f"imagenes/chr{cromosoma}.png"
if os.path.exists(ruta_imagen):
    imagen = Image.open(ruta_imagen)
    st.image(imagen, caption=f"Cromosoma {cromosoma}", use_column_width=True)
else:
    st.warning("Imagen no disponible para este cromosoma")

# Notas adicionales
st.caption("Datos genómicos de referencia - Versión 1.0")