#Criar uma varável para armazer o nome e a quantidade de experiência (XP) de um herói, 
#depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

# Se XP for menor que 1000 = Ferrro
# Se XP for menor que 1001 e 2000 = Bronze
# 2001 e 5000 = Prata ouro
# 5001 a 7000 = Ouro
# 7001 a 8000 = Platina 
# 8001 a 9000 = Ascendente 
# 90001 a 10000 = Imortal
# >= a 10001 = Radiante
a = "N"

while a != "S":
    nome  = input("Nome do herói = ")
    xp  = int(input("XP =  "))
    heroi = [nome, xp]
    print (heroi[1])
    if heroi[1] < 1000 :
        nivel = "Ferro"
    elif heroi[1]>1001 and heroi[1]<= 2000 :
        nivel = "Bronze"
    elif heroi[1]>2001 and heroi[1]<= 5000 :
        nivel = "Prata"
    elif heroi[1]>5001 and heroi[1]<= 7000 :
        nivel = "Ouro"
    elif heroi[1]>7001 and heroi[1]<= 8000 :
        nivel = "Platina"
    elif heroi[1]>7001 and heroi[1]<= 9000 :
        nivel= " Ascendente"
    elif heroi[1]>7001 and heroi[1]<= 10000 :
        nivel = "Imortal"
    elif heroi[1]> 10000 :
        nivel = "Radiante"

    print(f"O herói de nome {nome} está no nível de {nivel}")
    a = input("Sarir [S/N]  ")