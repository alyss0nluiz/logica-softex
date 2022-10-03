import pandas as pd

df = pd.read_csv("notas_alunos.csv")
df = df.set_index('aluno')
media = (df["nota_1"] + df["nota_2"])/2
df["media"] = media

df.loc[df["media"] >= 7 and df["faltas"] <= 5, "situação"] = "Aprovado"
df.loc[df["media"] < 7, "situação"] = "Reprovado"
df.loc[df["media"] > 5, "situação"] = "Reprovado"

df.to_csv("alunos_situacao.csv")