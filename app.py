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

# Estilos personalizados con bordes niquelados y fuente Minecraft
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');
    
    .main {
        background-color: #1E1E1E;
    }
    .stApp {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
    .element-container {
        border: 2px solid #808080;
        border-image: linear-gradient(45deg, #A8A8A8, #D3D3D3, #A8A8A8) 1;
        padding: 20px;
        margin: 10px 0;
        border-radius: 5px;
        background: linear-gradient(145deg, #1a1a1a, #2d2d2d);
        box-shadow: 0 0 15px rgba(168, 168, 168, 0.2);
    }
    .robot-title {
        font-family: 'VT323', monospace;
        font-size: 48px;
        text-align: center;
        color: #00ff00;
        text-shadow: 2px 2px #003300;
        margin-bottom: 20px;
    }
    .minecraft-text {
        font-family: 'VT323', monospace;
        font-size: 24px;
    }
    .diagnostic-box {
        background: #2d2d2d;
        border: 3px solid #808080;
        border-image: linear-gradient(45deg, #A8A8A8, #D3D3D3, #A8A8A8) 1;
        padding: 20px;
        margin: 10px 0;
        border-radius: 8px;
    }
    .robot-ascii {
        font-family: monospace;
        white-space: pre;
        font-size: 12px;
        color: #00ff00;
        text-align: center;
        margin: 20px 0;
    }
    .copyright {
        position: fixed;
        bottom: 10px;
        right: 10px;
        font-size: 12px;
        color: #666;
        font-family: 'VT323', monospace;
    }
    </style>
    
    <div class="robot-ascii">
     /\\___/\\
    (  o o  )
    (  =^=  ) 
     (______)
    </div>
    
    <div class="robot-title">🤖 Sistema Experto de Diagnóstico</div>
""", unsafe_allow_html=True)

# Inicializar el motor de diagnóstico
engine = DiagnosticoComputadora()

# Sidebar con información
with st.sidebar:
    st.markdown('<div class="minecraft-text">', unsafe_allow_html=True)
    st.image("https://via.placeholder.com/150?text=Tech+Support", width=150)
    st.header("⚙️ Panel de Control")
    st.info(f"Versión: {engine.__version__}")
    st.info(f"Autor: {engine.__author__}")
    st.markdown('</div>', unsafe_allow_html=True)

# Contenedor principal con estilo Minecraft
st.markdown('<div class="diagnostic-box minecraft-text">', unsafe_allow_html=True)
problema = st.selectbox(
    "🔍 Seleccione el problema que está experimentando:",
    [
        "Seleccione un problema...",
        "pantalla_negra",
        "sin_conexion_internet",
        "teclado_no_funciona",
        "audio_no_funciona"
    ]
)

if st.button("🔮 Diagnosticar") and problema != "Seleccione un problema...":
    engine.reset()
    engine.declare(Fact(problema=problema))
    engine.run()
    
    if engine.diagnostico_resultado:
        st.markdown('<div class="diagnostic-box">', unsafe_allow_html=True)
        col1, col2 = st.columns([2,1])
        
        with col1:
            st.markdown(f"### {engine.diagnostico_resultado['icono']} {engine.diagnostico_resultado['titulo']}")
            st.markdown("### 📋 Pasos sugeridos:")
            for i, sugerencia in enumerate(engine.diagnostico_resultado['sugerencias'], 1):
                st.markdown(f"{i}. {sugerencia}")
        
        with col2:
            st.metric(
                label="⚠️ Nivel de Gravedad",
                value=engine.diagnostico_resultado['gravedad']
            )
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer con copyright estilo Minecraft
st.markdown(
    f'<div class="copyright minecraft-text">{engine.__copyright__}</div>',
    unsafe_allow_html=True
)