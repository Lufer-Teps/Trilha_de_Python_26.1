#1coleta de dados do usuário.

monstro_1 = input("Boas vindas! Digite o nome do primeiro monstro: ")
vida_1 = int(input("Digite a vida do primeiro monstro: "))
if vida_1 <= 0:
    print("Vida inválida, evite começar a batalha ja perdendo!!.")
    exit()
ataque_1 = int(input("Digite o ataque do primeiro monstro: "))
if ataque_1 <= 0:
    print("Ataque inválido!! Um monstro precisa ter pelo menos 1 de ataque.")
    exit()
monstro_2 = input("Digite o nome do segundo monstro: ")
vida_2 = int(input("Digite a vida do segundo monstro: "))
if vida_2 <= 0:
    print("Vida inválida, evite começar a batalha ja perdendo!!.")
    exit()
ataque_2 = int(input("Digite o ataque do segundo monstro: "))
if ataque_2 <= 0:
    print("Ataque inválido!! Um monstro precisa ter pelo menos 1 de ataque.")
    exit()


#2)criação dos parametros pra função de ataque e placar.

def atacar(atacante, dano, defensor, hp_defensor):
    hp_defensor -= dano

    if hp_defensor < 0:
        hp_defensor = 0

    print(f"{atacante} ataca {defensor} causando {dano} de dano!")
    print(f"{defensor} ficou com {hp_defensor} de HP\n")

    return hp_defensor

def exibir_placar(nome1, hp1, nome2, hp2):
    print("===== PLACAR =====")
    print(f"{nome1}: {hp1} HP")
    print(f"{nome2}: {hp2} HP")
    print("==================\n")

#3) laço de repetição de turno.

turno= 1

while vida_1 > 0 and vida_2 > 0:
    print(f"--- Turno {turno} ---")

    exibir_placar(monstro_1, vida_1, monstro_2, vida_2)

    if turno % 2 != 0:
        vida_2 = atacar(monstro_1, ataque_1, monstro_2, vida_2)

        if vida_2 <= 0:
            print(f"{monstro_1} venceu a batalha!")
            break

    else:
        vida_1 = atacar(monstro_2, ataque_2, monstro_1, vida_1)

        if vida_1 <= 0:
            print(f"{monstro_2} venceu a batalha!")
            break
    turno += 1