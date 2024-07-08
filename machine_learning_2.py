import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://gist.githubusercontent.com/guilhermesilveira/1b7d5475863c15f484ac495bd70975cf/raw/16aff7a0aee67e7c100a2a48b676a2d2d142f646/projects.csv"
dados = pd.read_csv(url)

mapa = {
    "expected_hours": "horas_esperadas",
    "price": "preco",
    "unfinished": "nao_finalizado",
}
dados = dados.rename(columns=mapa)

troca = {
    0: 1,
    1: 0
}

dados["finalizado"] = dados.nao_finalizado.map(troca)

sns.scatterplot(x="horas_esperadas", y="preco", data=dados, hue="finalizado")

# plt.show()

x = dados[["horas_esperadas", "preco"]]
y = dados["finalizado"]

treino_x, teste_x, treino_y, teste_y = train_test_split(x, y, test_size=0.25, random_state=2, stratify=y)

modelo = LinearSVC(random_state=2)
modelo.fit(treino_x, treino_y)

previsoes = modelo.predict(teste_x)

accuracia = accuracy_score(teste_y, previsoes)
resultado = accuracia * 100

print("A acurácia foi %.2f%%" % resultado)