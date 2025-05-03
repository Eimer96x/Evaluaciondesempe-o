import streamlit as st
import pandas as pd

# Cargar automáticamente el dataset
df= pd.read_csv("sales_data_50_productos.csv")

# Título principal
st.title("📊 Análisis de Ventas (50 productos)")

# Menú lateral
st.sidebar.header("🔍 Filtros")

# Filtro por categoría
categorias = df["Category"].dropna().unique()
categoria_seleccionada = st.sidebar.selectbox("Selecciona una categoría", categorias)

# Filtro por rango de precios
min_precio = float(df["Price"].min())
max_precio = float(df["Price"].max())
rango_precio = st.sidebar.slider(
    "Rango de precios",
    min_value=min_precio,
    max_value=max_precio,
    value=(min_precio, max_precio)
)

# Filtrar los datos
df_filtrado = df[
    (df["Category"] == categoria_seleccionada) &
    (df["Price"] >= rango_precio[0]) &
    (df["Price"] <= rango_precio[1])
]

# Mostrar resultados
st.subheader(f"📋 Productos en categoría: {categoria_seleccionada}")
st.dataframe(df_filtrado)

# Métricas
st.subheader("📈 Métricas")
st.metric("Total de Ventas", f"${df_filtrado['Total_Sales'].sum():,.2f}")
st.metric("Precio Promedio", f"${df_filtrado['Price'].mean():,.2f}")
st.metric("Cantidad Total Vendida", int(df_filtrado['Quantity'].sum()))