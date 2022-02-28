# Alterar o valor de duas chaves do dicionário.
def alterar_dic(chave, chave2, dic):
    for key, value in dic.items():
        if key == chave or key == chave2:
            dic[key] = dic[key] + 1


# Alterar o valor de uma chave do dicionário.
def alterar_dic1(chave, dic):
    for key, value in dic.items():
        if key == chave:
            dic[key] = dic[key] + 1


# Diminui o valor de uma chave do dicionário.
def diminui_dic1(chave, dic):
    for key, value in dic.items():
        if key == str(chave):
            dic[key] = dic[key] - 1


# Perguta ao usuário se está satisfeito com a
# recomendação e altera o dicionário.
def good_or_bad(cafe, dic):
    q1 = input("\nFicaste feliz com a recomendação? "
               "Responda 'S' para SIM ou "
               "'N' para NÃO: ")
    q1 = q1.upper()
    while q1 != "S" and q1 != "N":
        print("\nCarregaste: ", q1)
        q1 = input("Carregue 'S' se está satisfeito ou, "
                   "'N' se não estiver: ")
        q1 = q1.upper()
    if q1 == "S":
        print("\nObrigado, aproveite o teu café!")
        alterar_dic1("happy", dic)
    else:
        print("\nPor favor, converse com o nosso barista. "
              "Ele irá te ajudar em uma nova escolha.")
        alterar_dic1("sad", dic)
        diminui_dic1(cafe, dic)
