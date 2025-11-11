import streamlit as st
import pandas as pd
import joblib

# Cargar el Modelo y las Columnas 

try:
    model = joblib.load('modelo_rf.joblib')
    features = joblib.load('features_simples.joblib')
except FileNotFoundError:
    st.error("Error: No se encontraron los archivos del modelo. Asegúrate de que 'modelo_rf.joblib' y 'features_simples.joblib' están en la carpeta.")
    st.stop()


# Título de la App
st.title(' Simulador de Precios de Airbnb en Valencia')
st.write('Usa los deslizadores para cambiar las características y predecir el precio.')

#  Crear los "Inputs" para el usuario
st.sidebar.header('Introduce las Características:')

# Usamos los valores medios/min/max de 'df.describe()' para poner límites lógicos
lat = st.sidebar.slider('Latitud', min_value=39.40, max_value=39.50, value=39.47, step=0.001, format="%.4f")
lon = st.sidebar.slider('Longitud', min_value=-0.42, max_value=-0.30, value=-0.37, step=0.001, format="%.4f")
min_nights = st.sidebar.number_input('Noches Mínimas', min_value=1, max_value=365, value=3)
num_reviews = st.sidebar.number_input('Número de Reseñas', min_value=0, max_value=1000, value=10)
reviews_month = st.sidebar.slider('Reseñas por Mes', min_value=0.0, max_value=10.0, value=1.5, step=0.1)
availability = st.sidebar.number_input('Disponibilidad (días/año)', min_value=0, max_value=365, value=200)

# Botón de Predicción
if st.sidebar.button('¡Predecir Precio!'):
    
    
    input_data = {
        'latitude': lat,
        'longitude': lon,
        'minimum_nights': min_nights,
        'number_of_reviews': num_reviews,
        'reviews_per_month': reviews_month,
        'availability_365': availability
    }
    
  
    input_df = pd.DataFrame([input_data], columns=features)

    
    try:
        precio_predicho = model.predict(input_df)
        
        # Mostrar el resultado
        st.subheader(f'El precio estimado por noche es:')
        st.markdown(f'## **{precio_predicho[0]:.2f} €**')
        
    except Exception as e:
        st.error(f"Error al predecir: {e}")