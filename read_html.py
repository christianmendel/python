import pandas as pd

url = "https://blog.toroinvestimentos.com.br/bolsa/empresas-que-pagam-dividendos/"

tabelas = pd.read_html(url)

tabela = tabelas[0]

tabela.columns = ['Empresa', 'Código', 'Dividend yield']

tabela['Dividend yield'] = tabela['Dividend yield'].str.replace('%', '').str.strip()

tabela['Dividend yield'] = tabela['Dividend yield'].str.split(',').str[0]

tabela['Dividend yield'] = pd.to_numeric(tabela['Dividend yield'], errors='coerce')

tabela_filtrada = tabela[tabela['Dividend yield'] > 5]

print(tabela.shape)
print(tabela_filtrada)
