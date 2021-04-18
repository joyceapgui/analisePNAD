### Objetivo: Análise PNAD Contínua

#### Importar bibliotecas
import numpy as np
import pandas as pd
import os

#### Definir diretório (ajustar de acordo com o diretório escolhido)
os.chdir('C:\\Users\\joyce\\OneDrive\\Joyce\\4intellingence\\analisePNAD\\base')

### Importar base de dados
pnad = pd.read_csv("pnad.csv")

### Limpar base de dados
## Excluir observações com dia de nascimento igual a 99
pnad = pnad[pnad["V2008"] != 99]

## Excluir gêmeos
# Criar variável de data de nascimento
pnad["nasc"] = pnad["V2008"].astype(str) + pnad["V20081"].astype(str) + pnad["V20082"].astype(str)
# Criar variável domicílio + data de nascimento + sexo que irá permitir identificar os gêmeos
pnad["gemeo"] = pnad["V1008"].astype(str) + pnad["nasc"].astype(str) + pnad["V2007"].astype(str)
# Excluir observações dos gêmeos (observações cuja variável gemeo aparece mais de uma vez na base)
pnad = pnad.drop_duplicates(subset="gemeo", keep = "first")

### Questão 1
## Pessoas ocupadas no 4 trimestre de 2019
pnad2019 = pnad[pnad["Ano"] == 2019]
pnad2019_ocupadas = pnad2019[pnad2019["VD4002"] == 1]
pessoas_ocupadas2019 = pnad2019_ocupadas["VD4002"].sum()
print("Pessoas ocupadas em 2019: ")
print(pessoas_ocupadas2019)

# Perfil dessas pessoas
print("Perfil da população ocupada em 2019")
# Sexo
pnad2019_ocupadas["V2007"] = pnad2019_ocupadas["V2007"].replace([1, 2], ["Homem", "Mulher"])
print("Perfil por sexo:")
print(pnad2019_ocupadas.groupby("V2007").count()["UF"])
# Escolaridade
pnad2019_ocupadas["VD3004"] = pnad2019_ocupadas["VD3004"].replace([1, 2, 3, 4, 5, 6, 7, 8, 9], ["Pré-escolar", "Alfabetização", "Regular EF", "EJA/ supletivo EF", "Regular EM", "EJA/ supletivo EM", "Graduação", "Mestrado", "Doutorado"])
print("Perfil por escolaridade:")
print(pnad2019_ocupadas.groupby("VD3004").count()["UF"])
# Idade
print("Perfil por idade:")
pnad2019_ocupadas.groupby("V2009").count()["UF"]
print("> Idade Máxima:")
print(pnad2019_ocupadas["V2009"].max())
print("> Idade Mínima:")
print(pnad2019_ocupadas["V2009"].min())
print("> Média de idade:")
print(pnad2019_ocupadas["V2009"].mean())
# Cor ou raça
print("Perfil por cor ou raça:")
pnad2019_ocupadas["V2010"] = pnad2019_ocupadas["V2010"].replace([1, 2, 3, 4, 5, 9], ["Branca", "Preta", "Amarela", "Parda", "Indígena", "Ignorado"])
print(pnad2019_ocupadas.groupby("V2010").count()["UF"])

## Pessoas ocupadas no 4 trimestre de 2020
pnad2020 = pnad[pnad["Ano"] == 2020]
pnad2020_ocupadas = pnad2020[pnad2020["VD4002"] == 1]
pessoas_ocupadas2020 = pnad2020_ocupadas["VD4002"].sum()
pessoas_ocupadas2020

# Perfil dessas pessoas
print("Perfil da população ocupada em 2020")
# Sexo
pnad2020_ocupadas["V2007"] = pnad2020_ocupadas["V2007"].replace([1, 2], ["Homem", "Mulher"])
print("Perfil por sexo:")
print(pnad2020_ocupadas.groupby("V2007").count()["UF"])
# Escolaridade
pnad2020_ocupadas["VD3004"] = pnad2020_ocupadas["VD3004"].replace([1, 2, 3, 4, 5, 6, 7, 8, 9], ["Pré-escolar", "Alfabetização", "Regular EF", "EJA/ supletivo EF", "Regular EM", "EJA/ supletivo EM", "Graduação", "Mestrado", "Doutorado"])
print("Perfil por escolaridade:")
print(pnad2020_ocupadas.groupby("VD3004").count()["UF"])
# Idade
print("Perfil por idade:")
pnad2020_ocupadas.groupby("V2009").count()["UF"]
print("> Idade Máxima:")
print(pnad2020_ocupadas["V2009"].max())
print("> Idade Mínima:")
print(pnad2020_ocupadas["V2009"].min())
print("> Média de idade:")
print(pnad2020_ocupadas["V2009"].mean())
# Cor ou raça
print("Perfil por cor ou raça:")
pnad2020_ocupadas["V2010"] = pnad2020_ocupadas["V2010"].replace([1, 2, 3, 4, 5, 9], ["Branca", "Preta", "Amarela", "Parda", "Indígena", "Ignorado"])
print(pnad2020_ocupadas.groupby("V2010").count()["UF"])

### Questão 2
## Ocupados
# Renda média efetiva
print("Renda média efetiva 2019:")
print(pnad2019_ocupadas["VD4020"].mean())
print("Renda média efetiva 2020:")
print(pnad2020_ocupadas["VD4020"].mean())

print("É possível observar que a renda média efetiva da população aumentou entre o 4º trimestre de 2019 e o mesmo período do ano seguinte.")

# Renda média habitual
print("Renda média habitual 2019:")
print(pnad2019_ocupadas["VD4019"].mean())
print("Renda média habitual 2020:")
print(pnad2020_ocupadas["VD4019"].mean())

print("É possível observar que a renda média habitual da população aumentou entre o 4º trimestre de 2019 e o mesmo período do ano seguinte.")

## Ocupados com redução de jornada
# Avaliar redução de jornada
pnad2019_ocupadas["red_jornada"] = (pnad2019_ocupadas["VD4031"]-pnad2019_ocupadas["VD4035"])/pnad2019_ocupadas["VD4031"]
pnad2020_ocupadas["red_jornada"] = (pnad2020_ocupadas["VD4031"]-pnad2020_ocupadas["VD4035"])/pnad2020_ocupadas["VD4031"]

# População ocupada com redução de jornada
pnad2019_redjornada = pnad2019_ocupadas[pnad2019_ocupadas["red_jornada"] <= 0.25]
pnad2019_redjornada = pnad2019_redjornada[pnad2019_redjornada["red_jornada"] >= 0]
pnad2020_redjornada = pnad2020_ocupadas[pnad2020_ocupadas["red_jornada"] <= 0.25]
pnad2020_redjornada = pnad2020_redjornada[pnad2020_redjornada["red_jornada"] >= 0]

# Renda média efetiva
print("Renda média efetiva 2019:")
print(pnad2019_redjornada["VD4020"].mean())
print("Renda média efetiva 2020:")
print(pnad2020_redjornada["VD4020"].mean())

print("É possível observar que a renda média efetiva da população aumentou entre o 4º trimestre de 2019 e o mesmo período do ano seguintepara a população com redução de jornada.")

# Renda média habitual
print("Renda média habitual 2019:")
print(pnad2019_redjornada["VD4019"].mean())
print("Renda média habitual 2020:")
print(pnad2020_redjornada["VD4019"].mean())

print("É possível observar que a renda média habitual da população aumentou entre o 4º trimestre de 2019 e o mesmo período do ano seguinte para a população com redução de jornada.")

## Ocupados, mas temporariamente afastados
# Ppulação ocupada, mas temporariamente afastada
pnad2019_afastadas = pnad2019_ocupadas[pnad2019_ocupadas["V4005"] == 1]
pnad2020_afastadas = pnad2020_ocupadas[pnad2020_ocupadas["V4005"] == 1]

# Renda média efetiva
print("Renda média efetiva 2019:")
print(pnad2019_afastadas["VD4020"].mean())
print("Renda média efetiva 2020:")
print(pnad2020_afastadas["VD4020"].mean())

print("É possível observar que a renda média efetiva da população aumentou entre o 4º trimestre de 2019 e o mesmo período do ano seguintepara a população temporariamente afastada.")

# Renda média habitual
print("Renda média habitual 2019:")
print(pnad2019_afastadas["VD4019"].mean())
print("Renda média habitual 2020:")
print(pnad2020_afastadas["VD4019"].mean())

print("É possível observar que a renda média habitual da população aumentou entre o 4º trimestre de 2019 e o mesmo período do ano seguinte para a população temporariamente afastada.")