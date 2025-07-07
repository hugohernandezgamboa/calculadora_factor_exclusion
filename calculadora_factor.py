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

st.set_page_config(page_title="Calculadora de Ingreso Bruto Mínimo", layout="centered")

st.title("Calculadora de Ingreso Bruto Mínimo para trabajadores de plataforma 📱")

st.write("Ingresa el **factor de exclusión** al que accediste el mes pasado y que te fue informado por la plataforma digital:")

# Entrada de usuario
factor = st.number_input("Factor de exclusión (%)", min_value=0.0, max_value=99.9, step=0.1, format="%.2f")

# Hacer el cálculo al presionar Enter
submit = st.button("Calcular ingreso bruto mínimo") or st.session_state.get("auto_submit", False)

if submit:
    if factor < 100:
        resultado = 8364 * 100 / (100 - factor)
        resultado_formateado = f"{resultado:,.2f}"
        st.success(f"✅ Debido al factor de exclusión al que accediste el mes pasado, tu Ingreso Bruto Mínimo para ser trabajador de plataforma debe ser de **${resultado_formateado}**.\n\nDe no alcanzar este monto, serás clasificado como **trabajador independiente**, manteniendo tu derecho a la seguridad social.")
    else:
        st.error("❌ El factor de exclusión no puede ser 100% o mayor.")

if "auto_submit" not in st.session_state:
    st.session_state.auto_submit = False

if factor != st.session_state.get("last_factor", None):
    st.session_state.auto_submit = True
    st.session_state.last_factor = factor
else:
    st.session_state.auto_submit = False
