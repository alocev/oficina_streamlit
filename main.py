import streamlit as st
import pandas as pd
import plotly.express as px

#configuração da página
st.set_page_config(
    page_title= "Painel de Indicadores Públicos",
    page_icon= "🥶",
    layout= "wide"
    )

#carregar dados
df = pd.read_csv('database/indicadores.csv', sep= ',')

#título do app
st.title("Painel de Indicadores de Governança Pública")
st.markdown("Simulação de dados públicos para auxiliar gestores na tomada de decisão.")

#filtros
estados = st.multiselect("Escolha os Estados", df['estado'].unique(), default=df['estado'].unique())
anos = st.slider("Escolha o intervalo de anos", int(df['ano'].min()), int(df['ano'].max()), (2021, 2022))

df_filtrado = df[(df['estado'].isin(estados)) & (df['ano'].between(*anos))]

#indicadores
col1, col2, col3 = st.columns(3)
col1.metric("📊 Alfabetização Média", f"{df_filtrado['alfabetizacao'].mean():.1f}%")
col2.metric("💼 Desemprego Médio", f"{df_filtrado['desemprego'].mean(): 1f}%")
col3.metric("💰Investimento em Saúde", f"R$ {df_filtrado['investimento_saude_milhoes'].mean():,.0f} mi")

#gráfico de alfabetização 
fig1 = px.line(df_filtrado, x="ano", y="alfabetizacao", color="estado", title="Evolução da Alfabetização")
st.plotly_chart(fig1, use_container_width=True)

#gráfico de criminalidade
fig2 = px.bar(df_filtrado, x="ano", y="criminalidade", color="estado", barmode="group", title="Evolução da Alfabetização")
st.plotly_chart(fig2, use_container_width=True)

#simulação de investimento
st.header("🔧 Simulação de Aumento de Investimento em Saúde")
incremento = st.slider("Aumentar orçamento em (%)", 0, 100, 10)
df_simulado = df_filtrado.copy()
df_simulado['investimento_saude_milhoes'] *= (1 + incremento / 100)

st.dataframe(df_simulado[['estado', 'ano', 'investimento_saude_milhoes']])

#frufru
st.button("finalizamos!!")
st.snow()

#exportar CSV
csv = df_simulado.to_csv(index=False).encode('utf-8')
st.download_button("⬇️ Baixar Simulação em CSV", csv, "simulação_indicadores.csv", "text/csv")