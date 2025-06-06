import streamlit as st
import pandas as pd

# Título do dashboard
st.title("Dashboard Financeiro")

# Carrega o CSV
try:
    df = pd.read_csv("MS_Financial Sample.csv", sep=";", on_bad_lines="skip")
except Exception as e:
    st.error(f"Erro ao carregar CSV: {e}")
    st.stop()

# Limpa nomes das colunas
df.columns = df.columns.str.strip()

# Prévia dos dados
st.subheader("Prévia dos dados")
st.write(df.head())

# Define colunas que serão usadas
coluna_valor = "Sales"
coluna_categoria = "Segment"

if coluna_valor in df.columns and coluna_categoria in df.columns:
    # Limpeza e conversão dos valores monetários
    df[coluna_valor] = (
        df[coluna_valor]
        .astype(str)
        .str.replace(r"[^0-9,-]", "", regex=True)   # Remove símbolos
        .str.replace(".", "", regex=False)          # Remove pontos (milhares)
        .str.replace(",", ".", regex=False)         # Converte vírgula em ponto decimal
        .replace("-", None)                         # Trata "-" como nulo
    )

    # Converte para float e substitui NaN por 0
    df[coluna_valor] = pd.to_numeric(df[coluna_valor], errors="coerce").fillna(0.0)

    # Agrupa e plota gráfico
    faturamento_segmento = df.groupby(coluna_categoria)[coluna_valor].sum().sort_values(ascending=False)
    st.subheader("Faturamento por Segmento")
    st.bar_chart(faturamento_segmento)

else:
    st.warning(f"Colunas '{coluna_categoria}' e/ou '{coluna_valor}' não encontradas.")

