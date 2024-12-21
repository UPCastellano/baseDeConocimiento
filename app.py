import streamlit as st
from diagnostico import DiagnosticoComputadora
from experta import Fact

# Configuración de la página
st.set_page_config(
    page_title="Sistema Experto de Diagnóstico",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos personalizados
st.markdown("""
    <style>
    .main {
        background-color: #1E1E1E;
    }
    .stApp {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
    .copyright {
        position: fixed;
        bottom: 10px;
        right: 10px;
        font-size: 12px;
        color: #666;
    }
    </style>
""", unsafe_allow_html=True)

# Título y descripción
st.title("🔧 Sistema Experto de Diagnóstico de Computadoras")
st.markdown("---")

# Inicializar el motor de diagnóstico
engine = DiagnosticoComputadora()

# Sidebar con información
with st.sidebar:
    st.image("https://via.placeholder.com/150?text=Tech+Support", width=150)
    st.header("Información del Sistema")
    st.info(f"Versión: {engine.__version__}")
    st.info(f"Autor: {engine.__author__}")

# Selección del problema
problema = st.selectbox(
    "Seleccione el problema que está experimentando:",
    [
        "Seleccione un problema...",
        "pantalla_negra",
        "sin_conexion_internet",
        "teclado_no_funciona",
        "audio_no_funciona"
    ]
)

if st.button("Diagnosticar") and problema != "Seleccione un problema...":
    # Realizar diagnóstico
    engine.reset()
    engine.declare(Fact(problema=problema))
    engine.run()
    
    if engine.diagnostico_resultado:
        # Mostrar resultados
        col1, col2 = st.columns([2,1])
        
        with col1:
            st.subheader(f"{engine.diagnostico_resultado['icono']} {engine.diagnostico_resultado['titulo']}")
            st.markdown("### Pasos sugeridos:")
            for i, sugerencia in enumerate(engine.diagnostico_resultado['sugerencias'], 1):
                st.markdown(f"{i}. {sugerencia}")
        
        with col2:
            st.metric(
                label="Nivel de Gravedad",
                value=engine.diagnostico_resultado['gravedad']
            )

# Footer con copyright
st.markdown(
    f"<div class='copyright'>{engine.__copyright__}</div>",
    unsafe_allow_html=True
)