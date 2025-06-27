import streamlit as st
import pandas as pd
import plotly.express as px

#formato da página
st.set_page_config(
    page_title = "Times Brasileiros - Análise",
    page_icon = "⚽",
    layout = "wide",
    initial_sidebar_state = "expanded"
    )

#carregamento de dados
df = pd.read_csv('database/times.csv', sep = ',')

#sidebar menu
st.sidebar.title = "CATEGORIAS"
categoria = st.sidebar.radio("", [
    "Início",
    "Libertadores",
    "Brasileirão",
    "Mundial",
    "Torcida",
    "Fundação",
    "Mascote"
])

#Início
if categoria == "Início":
    st.title("Ánalise de Times Brasileiros")
    st.markdown("""Este é meu primeiro aplicativo e mostra estatísticas de alguns dos grandes clubes brasileiros, com dados como: títulos, torcida, fundação e mascote.
            Selecione as categorias na barra lateral da página para navegar pelo app!!""")
    
#Libertadores
elif categoria == "Libertadores":
    st.title("🏆 Títulos da Libertadores")
    times_select = st.multiselect(
        "Selecione os times para comparação:",
        options = df["time"].unique().tolist(),
        default = df["time"].unique().tolist()
    )
    df_filtrado = df[df["time"].isin(times_select)]
    fig = px.bar(df_filtrado, x = "time", y = "libertadores", color = "time", text = "libertadores", title = "Títulos por Time")
    st.plotly_chart(fig, use_container_width = True)

#Brasileirão
elif categoria == "Brasileirão":
    st.title("🎖️ Títulos do Campeonato Brasileiro")
    times_select = st.multiselect(
        "Selecione os times para comparação:",
        options = df["time"].unique().tolist(),
        default = df["time"].unique().tolist(),
        key = "brasileirao_multiselect"
    )
    df_filtrado = df[df["time"].isin(times_select)]
    fig = px.bar(df_filtrado, x = "time", y = "brasileirão", color = "time", text = "brasileirão", title = "Títulos por Time")
    st.plotly_chart(fig, use_container_width = True)

#Mundial
elif categoria == "Mundial":
    st.title("🌎 Títulos do Mundial")
    times_select = st.multiselect(
        "Selecione os times para comparação:",
        options = df["time"].unique().tolist(),
        default = df["time"].unique().tolist(),
        key = "mundial_multiselect"
    )
    df_filtrado = df[df["time"].isin(times_select)]
    fig = px.bar(df_filtrado, x = "mundial", y = "time", orientation = "h", color = "time", text = "mundial",title = "Times Brasileiros com Títulos do Mundial")
    fig.update_layout(xaxis_title = "Títulos do Mundial", yaxis_title = "Time", showlegend = False)
    st.plotly_chart(fig, use_container_width = True)

#Torcida
elif categoria == "Torcida":
    st.title("🚩 Torcida por Time - em milhões")
    times_select = st.multiselect(
        "Selecione os times para comparação:",
        options = df["time"].unique().tolist(),
        default = df["time"].unique().tolist(),
        key = "torcida_multiselect"
    )
    df_filtrado = df[df["time"].isin(times_select)]
    fig = px.pie(df_filtrado, names = "time", values = "torcida(milhões)", title = "Participação das Torcidas por Time", color_discrete_sequence = px.colors.qualitative.Safe)
    fig.update_traces(textinfo = "label+value")
    fig.update_layout(title_x = 0.5, showlegend = True)
    st.plotly_chart(fig, use_container_width = True)

#Fundação
elif categoria == "Fundação":
    st.title("Fundação dos Times")
    df_ordenado = df.sort_values(by = "fundação")
    for index, row in df_ordenado.iterrows():
        with st.expander(f"📌 {row['time']}"):
            st.write(f"🏟️ Time: **{row['time']}**")
            st.write(f"🗓️ Fundado em: **{row['fundação']}**")

#Mascote
elif categoria == "Mascote":
    st.title("Mascotes dos Times")
    df_ordenado = df.sort_values(by = "time")
    col1, col2 = st.columns(2)
    for i, row in df_ordenado.iterrows():
        with (col1 if i % 2 == 0 else col2):
            st.subheader(f"⚽ {row['time']}")
            st.write(f"Mascote: **{row['mascote']}**")
            st.markdown("---")
   