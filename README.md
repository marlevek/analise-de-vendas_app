# Dashboard de Análise de Vendas

## Visão Geral do Projeto
Este projeto envolve a criação de um dashboard interativo para análise de dados de vendas endas usando Streamlit e Plotly. O objetivo é fornecer visualizações dinâmicas e interativas que ajudem a entender o desempenho de vendas, marketing, controle de estoque e outros aspectos relacionados a vendas.

## Objetivos
- Realizar análises de rentabilidade e desempenho de vendas.
- Visualizar o desempenho regional e o impacto dos gastos com marketing.
- Controlar o estoque e analisar o desempenho de produtos ao longo do tempo.
- Oferecer uma interface intuitiva para exportar dados filtrados em formatos CSV.

fonte de dados: https://www.kaggle.com/datasets/dsfelix/us-stores-sales 

O conjunto de dados inclui informações sobre vendas, lucro, despesas, marketing, estoque e muito mais, com as seguintes colunas:
- `Area Code`: Código da loja
- `State`: Estado da loja
- `Market`: Região da loja
- `Market Size`: Tamanho da loja
- `Profit`: Lucro em dólares
- `Margin`: Margem (Lucro + Despesas Totais ou Vendas - COGS)
- `Sales`: Valores adquiridos em vendas
- `COGS`: Custo das mercadorias vendidas
- `Total Expenses`: Despesas totais
- `Marketing`: Despesas em marketing
- `Inventory`: Valor do estoque no momento da venda
- `Budget Profit`: Lucro orçado
- `Budget COGS`: COGS orçado
- `Budget Margin`: Margem orçada
- `Budget Sales`: Vendas orçadas
- `ProductID`: ID do produto
- `Date`: Data da venda
- `Product Type`: Categoria do produto
- `Product`: Descrição do produto
- `Type`: Tipo

## Análise Exploratória
Antes de criar o dashboard, foi realizada uma análise exploratória dos dados para identificar inconsistências e preparar os dados para análise. Durante essa fase:
- Verifiquei a integridade dos dados e identifiquei possíveis problemas.
- Transformei a coluna `Date` para o formato de data usando o código:
 ```python
  df['Date'] = pd.to_datetime(df['Date']).dt.date

Autor: Marcelo
Licença: GPL-3.0 license