import streamlit as st
# Estilos con colores institucionales STYFE
st.markdown("""
    <style>
        h1 {
            color: #9F2241;
        }
        .stNumberInput input {
            background-color: #235B4E;
            color: white;
        }
        .stButton>button {
            background-color: #235B4E;
            color: white;
            border-radius: 8px;
        }
        .stSuccess {
            background-color: #BC955C !important;
            color: black !important;
        }
    </style>
""", unsafe_allow_html=True)
st.set_page_config(page_title="Calculadora de Ingreso Bruto", layout="centered")

st.title("Calculadora de Ingreso Bruto Mínimo 🧮")
st.write("Ingresa el **factor de exclusión** al que accediste el mes pasado:")

# Entrada del usuario
factor = st.number_input("Factor de exclusión (%)", min_value=0.0, max_value=99.9, step=0.1)

# Botón para calcular
if st.button("Calcular ingreso bruto mínimo"):
    if factor < 100:
        resultado = 8364 * 100 / (100 - factor)
        resultado = round(resultado, 2)
        st.success(f"✅ Debido al factor de exclusión al que accediste el mes pasado, tu Ingreso Bruto Mínimo para ser trabajador de plataforma debe ser de ${resultado}.")
    else:
        st.error("❌ El factor de exclusión no puede ser 100% o mayor.")
