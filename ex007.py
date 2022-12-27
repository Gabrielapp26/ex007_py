#Desafio 06
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar 
print("Escreve quanto de dinheiro você tem e saiba quantos dólares você pode comprar")
r = int(input("Valor em reais: "))
d = r/5.32  #preço do dólar 12/12/2022
print("Com {} reais, você poderá comprar {:.2f} dólares".format(r,d))