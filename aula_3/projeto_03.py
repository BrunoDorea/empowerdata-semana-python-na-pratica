import pandas as pd
import plotly_express as px

dados = pd.read_excel("../__docs/vendas.xlsx")

# agrupando dados de forma de pagamento por cidade e gerando uma tabela no excel
dados.groupby(["cidade", "forma_pagamento"]).preco.sum().to_excel('analise_forma_pagamento.xlsx')

# criando gráficos
colunas = ['loja', 'cidade', 'estado', 'forma_pagamento', 'regiao', 'tamanho', 'local_consumo']
# looping for
for coluna in colunas:
  grafico = px.histogram(dados, x=coluna, y="preco", text_auto = True, color="forma_pagamento")
  grafico.show()