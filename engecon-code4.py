import pandas as pd

df = pd.read_csv("df.csv", sep = ";")

print(df.head(10))

tam = len(df)
lista_P = []
lista_K = []
vpl = 0

for l in range(0,350000,1):
    vpl=0
    lista_P.append(l)

    for i in range(0,tam,1):
        print(i)
        pk = df["FLUXO DE CAIXA FINAL"][i] / ((1+(l/100000))**i)
        vpl = pk + vpl

    lista_K.append(round(vpl,0))

print(lista_K)
print(lista_P)

lista_P1 =[]

for x in range(0,len(lista_P),1):
    lista_P1.append(lista_P[x]/100000)


df2 = pd.DataFrame({
    "Juros":lista_P1,
    "VPL":lista_K
})

df2.to_csv("arquivofinal1.csv")