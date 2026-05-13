# CALCULADORA METABÓLICA PRO - MÉTODO CLÓNATE
import streamlit as st

st.title("🛡️ Sistema de Optimización Nutricional")
st.write("Calcula tu déficit estratégico para transformar tu físico.")

# Entradas de usuario
peso = st.number_input("Tu peso actual (kg):", value=85.0)
objetivo_peso = st.number_input("Tu peso objetivo (kg):", value=78.0)
actividad = st.selectbox("Nivel de actividad:", ["Sedentario", "Moderado (3-4 días)", "Atleta (6+ días)"])

# Lógica de cálculo (Ingeniería Nutricional)
tdee_base = peso * 22  # TMB estimada
multiplicadores = {"Sedentario": 1.2, "Moderado (3-4 días)": 1.4, "Atleta (6+ días)": 1.7}
tdee_total = tdee_base * multiplicadores[actividad]

# Déficit estratégico
calorias_dieta = tdee_total - 400

st.divider()
st.subheader("📊 Tus Resultados Élite")
st.write(f"**Gasto Metabólico (TDEE):** {int(tdee_total)} kcal")
st.write(f"**Calorías para Perder Grasa:** {int(calorias_dieta)} kcal")

st.info(f"Para llegar a tus {objetivo_peso}kg, sigue el plan de la libreta.")
