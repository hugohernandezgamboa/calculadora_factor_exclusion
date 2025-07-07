import streamlit as st

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
