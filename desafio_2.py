#1 coleta de dados do usuário.

monstro_1 = input("Digite o nome do primeiro monstro: ")
vida_1 = int(input("Digite a vida do primeiro monstro: "))
ataque_1 = int(input("Digite o ataque do primeiro monstro: "))
monstro_2 = input("Digite o nome do segundo monstro: ")
vida_2 = int(input("Digite a vida do segundo monstro: "))
ataque_2 = int(input("Digite o ataque do segundo monstro: "))

resultado_1= ataque_1- vida_2
resultado_2= ataque_2 -vida_1 
#2 criação dos parametros pra função de ataque e placar.

def atacar(atacante_1, ataque_do_atacante_1, defensor_2, hp_defensor_2):
    
    atacar(monstro_1, ataque_1, monstro_2, resultado_1 )
    print(f"{atacante_1} ataca {defensor_2} causando {ataque_do_atacante_1} de dano! O defensor está com {hp_defensor_2}")


    