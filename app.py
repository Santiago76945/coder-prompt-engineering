import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

# Cargar variables de entorno
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Crear el cliente con la nueva API
client = OpenAI(api_key=api_key)

st.title("La receta que estás buscando")
st.write("Ingresa los datos para generar una receta:")

# Campos de entrada
recipe_name = st.text_input("Nombre de la receta (opcional)")
ingredients = st.text_area("Ingredientes imprescindibles (opcional)")
time_option = st.radio("Tiempo de preparación", ("Menos de 30 minutos", "Menos de 1 hora", "No importa"))
difficulty = st.radio("Nivel de dificultad", ("Fácil", "No importa"))
dietary_options = st.multiselect("Preferencias dietéticas", ["Vegetariano", "Vegano", "Sin gluten", "Bajo en carbohidratos", "Bajo en grasa", "Bajo en calorías"])
other_diet = st.text_input("Otra preferencia (opcional)")
meal_type = st.selectbox("Tipo de comida", ["Desayuno", "Cena", "Postre", "Indiferente"])

if st.button("Generar receta"):
    # Armado del prompt
    prompt = "Genera una receta"
    if recipe_name:
        prompt += f" llamada {recipe_name}"
    if ingredients:
        prompt += f" que incluya los ingredientes: {ingredients}"
    if time_option != "No importa":
        prompt += f", con un tiempo de preparación {time_option}"
    if difficulty != "No importa":
        prompt += f", de nivel {difficulty}"
    if dietary_options:
        prompt += f", adecuada para: {', '.join(dietary_options)}"
    if other_diet:
        prompt += f" y {other_diet}"
    if meal_type != "Indiferente":
        prompt += f", ideal para {meal_type}"
    prompt += "."

    st.write("Enviando prompt a la IA...")
    
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.7,
    max_tokens=500  
    )
    receta = response.choices[0].message.content.strip()

    
    receta = response.choices[0].message.content.strip()
    st.subheader("Receta Generada:")
    st.write(receta)
