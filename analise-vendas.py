import streamlit as st
import pandas as pd
import plotly.express as px
from io import BytesIO

st.set_page_config('Análise de Vendas', page_icon=':chart_with_upwards_trend:', layout='centered')

# Carregar os dados (exemplo usando um CSV)
@st.cache_data
def load_data():
    df = pd.read_csv('sales_treated.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    return df

# Função para download de dados
def download_data(df):
    buffer = BytesIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)
    return buffer

# Função principal
def main():
    st.title('Dashboard de Análise de Vendas')
    st.subheader('Período: 2010 - 2011')
    
    # carregar dados
    df = load_data()
    
    # Definir intervalo de datas com base no DataFrame
    min_date = df['Date'].min().date()
    max_date = df['Date'].max().date()
      
    # Exibir o DataFrame no app
    st.write('Visualizando os primeiros dados')
    st.write(df.head())
    
    # Sidebar para escolher a análise
    st.sidebar.image('logo_empresa.png')
    st.sidebar.title('Escolha a Análise')
    analysis = st.sidebar.selectbox("Selecione a análise", 
                                    ["Desempenho de Vendas", "Análise de Rentabilidade", "Visualização de Desempenho Regional",
                                     "Análise de Marketing", "Controle de Estoque", "Análise Temporal", "Análise de Produto"])
    # Filtros dinâmicos
    st.sidebar.title('Filtros')
    state_filter = st.sidebar.multiselect('Selecione o Estado ou Estados', df['State'].unique())
    product_filter = st.sidebar.multiselect('Selecione o Produto ou Produtos', df['Product'].unique())

    # Filtro de período com base nas datas do DataFrame
    date_filter = st.sidebar.date_input("Selecione o Período", [min_date, max_date], min_value=min_date, max_value=max_date)
    
    # Aplicar filtros aos dados
    if state_filter:
        df = df[df['State'].isin(state_filter)]
    if product_filter:
        df = df[df['Product'].isin(product_filter)]
    if date_filter:
        start_date, end_date = pd.to_datetime(date_filter)
        df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    # Verificar se há dados após a aplicação dos filtros
    if df.empty:
        st.write('Nenhum dado disponível com os filtros selecionados')
        return
    
    # Exibir a análise selecionada
    if analysis == "Análise de Rentabilidade":
        st.header("Análise de Rentabilidade")
        fig = px.bar(df, x='State', y='Profit', color='Market', title="Lucro por Estado e Região")
        st.plotly_chart(fig)

    elif analysis == "Desempenho de Vendas":
        st.header("Desempenho de Vendas")
        fig = px.bar(df, x='State', y='Sales', color='Market', title="Vendas por Estado e Região")
        st.plotly_chart(fig)

    elif analysis == "Visualização de Desempenho Regional":
        st.header("Desempenho Regional")
        fig = px.bar(df, x='Market', y='Profit', title="Desempenho de Lucro por Região")
        st.plotly_chart(fig)
    
    elif analysis == 'Análise de Marketing':
        st.header('Análise de Marketing')
        fig = px.scatter(df, x='Marketing', y='Profit', color='State', size='Sales', title='Lucro em função dos gastos com marketing e vendas')
        st.plotly_chart(fig)
        
    elif analysis == 'Controle de Estoque':
        st.header('Controle de Estoque')
        fig = px.bar(df, x='State', y='Inventory', color='Product Type', title="Valor do Estoque por Estado e Categoria de Produto")
        st.plotly_chart(fig)

    elif analysis == "Análise Temporal":
        st.header("Análise Temporal")
        fig = px.line(df, x='Date', y='Sales', color='State', title="Vendas ao Longo do Tempo")
        st.plotly_chart(fig)

    elif analysis == "Análise de Produto":
        st.header("Análise de Produto")
        fig = px.bar(df, x='Product', y='Profit', color='Product Type', title="Lucro por Produto e Categoria")
        st.plotly_chart(fig)

    # Funcionalidade adicional: download dos dados filtrados
    st.subheader("Exportar Dados")
    if st.button("Baixar CSV"):
        csv = download_data(df)
        st.download_button(label="Download CSV", data=csv, file_name='dados_filtrados.csv', mime='text/csv')

if __name__ == '__main__':
    main()