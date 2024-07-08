import yfinance as yf

acoes = ["BBAS3.SA", "BBSE3.SA"]

data = yf.download(acoes, period="1y")

data = data.head(3)
cotacoes = data.stack(level = 1)

print(cotacoes)