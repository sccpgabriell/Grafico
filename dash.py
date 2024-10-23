import streamlit as st
import plotly.express as px

def graficos(df_selecionado):
    if df_selecionado.empty:
        st.warning("Nenhum dado disponível para gerar gráficos")
        return

    graf1, graf2, graf3, graf4, graf5, graf6, graf7 = st.tabs(
        ["Gráfico de Barras", "Gráfico de Linhas", "Gráfico de Pizza", "Gráfico de Dispersão", "Gráfico de Área", "Gráfico de Histograma"]
    )

    with graf1:
        st.write("Gráfico de Barras")
        investimento = df_selecionado.groupby("marca").count()[["valor"]].sort_values(by="valor", ascending=False)

        fig_valores = px.bar(investimento,
                             x=investimento.index,
                             y="valor",
                             orientation="h",
                             title="<b>Valores de Carros</b>",
                             color_discrete_sequence=["#003b3"])
        st.plotly_chart(fig_valores, use_container_width=True)

    with graf2:
        st.write("Gráfico de Linhas")
        dados = df_selecionado.groupby("marca").count()[["valor"]]

        fig_valores2 = px.line(dados,
                               x=dados.index,
                               y="valor",
                               title="<b>Valores por Marca</b>",
                               color_discrete_sequence=["#0083b8"])
        st.plotly_chart(fig_valores2, use_container_width=True)

    with graf3:
        st.write("Gráfico de Pizza")
        dados2 = df_selecionado.groupby("marca").sum()[["valor"]]

        fig_valores3 = px.pie(dados2,
                              values="valor",
                              names=dados2.index,
                              title="<b>Distribuição de Valores por Marca</b>")
        st.plotly_chart(fig_valores3, use_container_width=True)

    with graf4:
        st.write("Gráfico de Dispersão")
        dados3 = df_selecionado.melt(id_vars=["marca"], value_vars=["valor"])

        fig_valores4 = px.scatter(dados3,
                                  x="marca",
                                  y="valor",
                                  color="variable",
                                  title="<b>Dispersão de Valores por Marca</b>")
        st.plotly_chart(fig_valores4, use_container_width=True)

    with graf5:
        st.write("Gráfico de Área")
        dados4 = df_selecionado.groupby("marca").sum()[["valor"]]

        fig_valores5 = px.area(dados4,
                               x=dados4.index,
                               y="valor",
                               title="<b>Área de Valores por Marca</b>")
        st.plotly_chart(fig_valores5, use_container_width=True)

    with graf6:
        st.write("Gráfico de Histograma")
        dados5 = df_selecionado.groupby("marca").sum()[["valor"]]
        
        fig_valores6 = px.histogram(dados5,
                                    x="valor",
                                    nbins=20,
                                    title="<b>Histograma de Valores</b>")
        st.plotly_chart(fig_valores6, use_container_width=True)

# Função para a barra de progresso
def barraprogresso():
    valorAtual = 100000  # Exemplo de valor atual
    objetivo = 200000
    percentual = round((valorAtual / objetivo) * 100)

    st.write(f"Você tem {percentual}% de {objetivo}. Corra atrás!")

    mybar = st.progress(0)
    for percentualCompleto in range(percentual):
        mybar.progress(percentualCompleto + 1)

# Função para menu lateral
def menuLateral():
    with st.sidebar:
        selecionado = st.selectbox("Menu", options=["Home", "Progresso"])

    if selecionado == "Home":
        st.subheader(f"Página: {selecionado}")
        graficos(df_selecionado)

    if selecionado == "Progresso":
        st.subheader(f"Página: {selecionado}")
        barraprogresso()

# Exemplo de execução
# df_selecionado = pd.DataFrame()  # Insira aqui o DataFrame que será usado
# menuLateral()
