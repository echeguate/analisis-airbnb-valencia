# 📊 Análisis y Predicción de Precios de Airbnb en Valencia

Este es un proyecto de portfolio completo para el Grado en Ciencia de Datos e IA (UMH). El proyecto cubre el ciclo de vida completo de la ciencia de datos: análisis exploratorio, entrenamiento de un modelo de machine learning y despliegue de una aplicación web interactiva.

---

## 🚀 App Web Interactiva (Simulador de Precios)

¡Puedes probar el modelo tú mismo! He desplegado una aplicación web con Streamlit donde puedes ajustar las características de un apartamento y obtener una predicción de precio en tiempo real.

### ➡️ **Prueba la app aquí:** [https://echeguate-analisis-airbnb-valencia-app-r9morl.streamlit.app/]



---

## 📖 Contenido del Repositorio

1.  **`analisis_airbnb.ipynb`**: Notebook de Jupyter con todo el Análisis Exploratorio de Datos (EDA).
2.  **`prediccion_airbnb.ipynb`**: Notebook de Jupyter que entrena y evalúa el modelo de Machine Learning.
3.  **`app.py`**: El código Python (Streamlit) para la aplicación web interactiva.
4.  **`modelo_rf.joblib`**: El archivo del modelo Random Forest entrenado.

---

# 1. Parte 1: Análisis Exploratorio (EDA)

El objetivo era responder a tres preguntas clave sobre el mercado de Airbnb en Valencia:

1.  ¿Cuáles son los barrios más caros para alquilar?
2.  ¿Qué tipo de propiedades dominan el mercado?
3.  ¿Existe una relación clara entre el precio y la popularidad (nº de reseñas)?

#### Conclusiones del Análisis:

* **Conclusión 1 (Barrios):** El barrio 'Pinedo' y 'El Saler' son los más caros de media, mostrando una clara segmentación por zonas premium. El análisis demuestra que el mercado está geográficamente segmentado por precio. Un inversor podría usar este mapa para identificar las zonas de mayor rentabilidad.

* **Conclusión 2 (Tipo de Propiedad):** El mercado está totalmente dominado por 'Apartamentos Enteros' (Entire home/apt), que representan más del 70% de la oferta. Las 'Habitaciones Privadas' son una segunda opción saludable (~2,000), pero el resto de categorías son estadísticamente irrelevantes. Esto define el tipo de turismo que atrae la plataforma en la ciudad.

* **Conclusión 3 (Precio vs. Reseñas):** La popularidad de un Airbnb en Valencia no la decide su precio. Depende de otros factores mucho más importantes (ubicación, calidad, limpieza), pero no es ni más popular por ser más barato ni por ser más caro.

---

# 2. Parte 2: Modelo de Machine Learning (Predicción)

Usé los datos limpios para entrenar un modelo de IA capaz de predecir el precio por noche de un alojamiento.

* **Modelo Utilizado:** `RandomForestRegressor` (de Scikit-Learn), elegido por su alta precisión y su capacidad para "explicar" sus decisiones.
* **Resultado:** El modelo es capaz de predecir el precio de un alojamiento con un **Error Medio Absoluto (MAE) de unos 126.02 €**.
* **Conclusión Clave (Importancia de Características):** El análisis del modelo revela que **la ubicación (latitud y longitud)** es, con diferencia, el factor más importante para determinar el precio en Valencia. Otros factores como las reseñas o la disponibilidad tienen un impacto mucho menor.



---

### ## 🛠️ Tecnologías Utilizadas

* **Python**
* **Pandas** (para la manipulación y limpieza de datos)
* **Matplotlib** y **Seaborn** (para visualización)
* **Scikit-Learn (sklearn)** (para construir y evaluar el modelo de ML)
* **Joblib** (para guardar el modelo entrenado)
* **Streamlit** (para construir la aplicación web interactiva)
* **Jupyter Notebook** (en VS Code)
