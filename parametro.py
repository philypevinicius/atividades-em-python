def porcento (s, d=8/100):
    s = s*d
    return (f'R${s:.2f}'). replace(".",",")

valor = porcento(1000)
print(valor)