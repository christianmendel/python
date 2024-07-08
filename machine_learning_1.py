import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

url = "https://gist.githubusercontent.com/guilhermesilveira/2d2efa37d66b6c84a722ea627a897ced/raw/10968b997d885cbded1c92938c7a9912ba41c615/tracking.csv"
dados = pd.read_csv(url)

mapa = {
    "home": "principal",
    "how_it_works": "como_funciona",
    "contact": "contato",
    "bought": "comprou"
}
dados = dados.rename(columns=mapa)

x = dados[["principal", "como_funciona", "contato"]]
y = dados["comprou"]

treino_x = x[:75]
treino_y = y[:75]

teste_x = x[75:]
teste_y = y[75:]

# modelo = LinearSVC(random_state=2)
# modelo.fit(treino_x, treino_y)

# previsoes = modelo.predict(teste_x)

# accuracia = accuracy_score(teste_y, previsoes)
# resultado = accuracia * 100

# print("A acurácia foi %.2f%%" % resultado)


# Outro modo de separar o treino e o teste
treino_x, teste_x, treino_y, teste_y = train_test_split(x, y, test_size=0.25, random_state=2, stratify=y)

modelo = LinearSVC(random_state=2)
modelo.fit(treino_x, treino_y)

previsoes = modelo.predict(teste_x)

accuracia = accuracy_score(teste_y, previsoes)
resultado = accuracia * 100

print("A acurácia foi %.2f%%" % resultado)
