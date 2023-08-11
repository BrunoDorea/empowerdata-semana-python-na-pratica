import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly

ticker = input("Digite o códig da Ação: ")
dados = yf.Ticker(ticker).history("2y")

# tratando os dados
treinamento = dados.reset_index()
treinamento = treinamento[["Date", "Close"]]
treinamento["Date"] = treinamento["Date"].dt.date
treinamento.columns = ["ds", "y"]
treinamento

modelo = Prophet()
modelo.fit(treinamento)
periodo = modelo.make_future_dataframe(90)
previsoes = modelo.predict(periodo)
plot_plotly(modelo, previsoes)