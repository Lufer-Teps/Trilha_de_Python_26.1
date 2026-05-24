#coleta de informações do usuário.


orcamento= float (input("Boas vindas a calcuadora de viagem, por favor digite o seu orçamento em reais."))
if orcamento <= 0:
    print("Orçamento inválido, por favor digite um valor positivo.")
    exit()
destino= (input("Qual o destino da viagem ? "))
passagem=float (input("Qual o custo da passagem ? "))
if passagem <= 0:
    print("Custo da passagem inválido, por favor digite um valor positivo.")
    exit()  
diaria=float (input("digite o valor da sua diária em euros."))
if diaria <= 0:
    print("Valor da diária inválido, por favor digite um valor positivo.")
    exit()
tempo=int (input("quantos dias voce ficara no país de destino ? "))
if tempo <= 0:
    print("Tempo de estadia inválido, por favor digite um valor positivo.")
    exit()

#variaveis essenciais.
conversao= (diaria * 6.1)

valor_da_hospedagem= (conversao * tempo)

custo_total= (passagem + valor_da_hospedagem)

dinheiro_restante= (orcamento - custo_total)
dinheiro_pendente= (custo_total - orcamento)

#informações finais pro usuario.
if custo_total >= orcamento:
    viagem_invalida=("Seu orçamento é inferior ao custo da viagem, logo ela é inválida. ")
    print(f"sua viagem não foi possivel pois o seu orçamento de {orcamento} é inferior ao custo da viagem de {custo_total}. Você ainda precisa de {dinheiro_pendente}.")
else:
    
    print(f"Sua viagem é válida Aproveite ! informações finais: o seu orçamento é de {orcamento} reais. Sua viagem para {destino} durará {tempo}. O custo da sua hospedagem será de {valor_da_hospedagem} o custo total da viagem sera de {custo_total} e ainda sobrará {dinheiro_restante}. ")

