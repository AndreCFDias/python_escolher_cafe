""" Indicar o uso da biblioteca Json. Irei usar para
    buscar uma biblioteca (meu banco de dados) em *.txt e
    depois sobrescrever o arquivo com a atualização
    das informações colhidas."""
import json
# Importar funções de outro arquivo *.py que serão utilizadas
from functions import alterar_dic, good_or_bad, alterar_dic1

# Importar um dicionário (meu banco de dados) de um arquivo *.txt
dicionario = json.load(open("dicionario.txt"))

# Importar a palavra passe de um arquivo *.txt
p_s = open('ps.txt', 'r')
palavra_passe = p_s.read()

inicio = input("\nBem vindo ao Âme Coffee!\n"
               "Estás pronto para iniciar a tua experiência? "
               "carregue '1' \n"
               "Para obter dados sobre as vendas de café, "
               "introduza a palavra-passe: ")

# Evitar que o usuário realize algo que nao foi pedido.
while inicio != "1" and inicio != palavra_passe:
    print("\nCarregaste: ", inicio)
    inicio = input("\nPor favor, "
                   "responda somente com '1' para iniciar, \n"
                   "ou a palavra-passe correta: ")

# Inicia-se o caminho de escolha do usuário.
if inicio == "1":
    p_s.close()
    sabe = input("\nÉs decidido e já sabe o que vais beber?\n"
                 "Carregue 'S' e podes ir ter com o barista. "
                 "Se precisas de ajuda, carregue 'A': ")
    # Padronizar letra maiuscula. Evita erro do usuário.
    sabe = sabe.upper()
    # Evitar que o usuário realize algo que nao foi pedido.
    while sabe != "S" and sabe != "A":
        print("\nCarregaste: ", sabe)
        sabe = input("\nPor favor, "
                     "responda somente com 'S' "
                     "se já sabes o que irá pedir\n"
                     "ou 'A' se precisas de ajuda: ")
        sabe = sabe.upper()

    if sabe == "S":  # Sabe o que vai pedir.
        print("\nFeliz em saber que já sabes o que quer!\n"
              "Peça ao nosso barista e BOM CAFÉ!")
        # Função criada para alterar os dados do Dicionário.
        alterar_dic("decididos", "total_cl", dicionario)
    # Nao sabe o que pedir -> segue o caminho de auxilio à escolha.
    else:
        print("\nEntão vou te ajudar.")
        # Café Puro ou com Leite.
        puro_leite = input("Se gostas de café PURO, carregue '1'.\n"
                           "Preferes café com LEITE? carregue '2': ")
        while puro_leite != "1" and puro_leite != "2":
            print("\nCarregaste no ", puro_leite)
            puro_leite = input("Por favor, responda somente com '1' "
                               "para café PURO,\n"
                               "ou '2' para café com LEITE: ")
        # Café puro.
        if puro_leite == "1":
            suave_intenso = input("\nSe gostas de café mais suave,\n"
                                  "onde os aromas e sabores são "
                                  "mais delicados, carregue '1'.\n"
                                  "Se preferes um café mais encorpado "
                                  "e com sabor intenso carregue '2': ")
            while suave_intenso != "1" and suave_intenso != "2":
                print("\nCarregaste ", suave_intenso)
                suave_intenso = input("Por favor, responda somente "
                                      "com '1' "
                                      "para um café SUAVE,\n "
                                      "ou '2' se "
                                      "preferes algo mais INTENSO: ")
            # Café suave -> V60.
            if suave_intenso == "1":
                print("\nAcredito que o método de preparo V60 "
                      "é o mais indicado.\n"
                      "O café demora cerca de 3 minutos "
                      "para ser filtrado.\n"
                      "Beba o café devagar, "
                      "perceba cada sabor que encontras. "
                      "Quase como um ritual de chá.\n"
                      "Mas não se engane, apesar de leve no paladar, "
                      "possui um nível de cafeina bem elevado! "
                      "Ótimo para iniciar o dia, ou receber aquela "
                      "energia que está a lhe faltar.")

                # Coleta de dados.
                alterar_dic("V60", "total_cl", dicionario)
                # Experiência foi boa ou ruim? Coleta de dados.
                good_or_bad("V60", dicionario)
            # Pequeno ou grande.
            else:
                grande_pequeno = input("\nCarregue '1' "
                                       "se quer um café em grande!\n"
                                       "Carregue '2' se preferes "
                                       "um mais pequeno: ")
                while grande_pequeno != "1" and grande_pequeno != "2":
                    print("\nCarregaste: ", grande_pequeno)
                    grande_pequeno = input("Por favor, Carregue '1' "
                                           "se quer um café grande,\n"
                                           "ou carregue '2' para "
                                           "um mais pequeno: ")
                # Café grande -> Espresso Duplo.
                if grande_pequeno == "1":
                    print("\nPodes pedir um ESPRESSO DUPLO. "
                          "Receberá um Double Shot do "
                          "nosso espresso delicioso\n"
                          "Não irá arrepender-se!!")
                    alterar_dic("Espresso duplo",
                                "total_cl", dicionario)
                    good_or_bad("Espresso duplo", dicionario)
                # Café pequeno -> Expresso.
                else:
                    print("\nVais de ESPRESSO SIMPLES, "
                          "ou se queres ser mais direto: CAFÉ\n"
                          "Sabias que o café espresso, é escrito "
                          "com a letra 'S'?\n"
                          "É uma palavra de origem italiana, "
                          "por isso, quando ler a ementa e lá "
                          "estiver eSpresso, a escrita está correta!")
                    alterar_dic("Espresso", "total_cl", dicionario)
                    good_or_bad("Espresso", dicionario)
        # Café com leite.
        else:
            gde_peq = input("\nQueres um café grande, quentinho"
                            " e bem confortável? Carregue '1'.\n"
                            "Se acreditas que os melhores perfumes "
                            "estão nos menores frascos,"
                            " carregue '2': ")
            while gde_peq != "1" and gde_peq != "2":
                print("\nCarregaste: ", gde_peq)
                gde_peq = input("Carregue '1' "
                                "se quer um café grande, ou\n"
                                "carregue '2' se preferes um "
                                "mais pequenino: ")
            # Grande com leite.
            if gde_peq == "1":
                leite = input("\nSe gostas mesmo de café e quer "
                              "mais café do que leite, carregue '1'\n"
                              "Agora, se és daqueles que preferes "
                              "muita espuma e uma bebida "
                              "muito cremosa, carregue '2': ")
                while leite != "1" and leite != "2":
                    print("Carregaste: ", leite)
                    leite = input("\nSe preferes mais café do "
                                  "que leite, carregue '1'\n"
                                  "Se queres mais leite do que "
                                  "café, carregue '2': ")
                # Mais café do que leite -> Flat White.
                if leite == "1":
                    print("\nO teu café será o moderninho "
                          "FLAT WHITE!\n"
                          "Duas doses do nosso espresso e "
                          "leite com pouca crema.\n"
                          "O sabor do café é evidente, porém, "
                          "o leite te transporta "
                          "para um lugar acolhedor.")
                    alterar_dic("Flat White", "total_cl", dicionario)
                    good_or_bad("Flat White", dicionario)
                # Mais leite do que café -> Cappuccino.
                else:
                    print("\nAh! Não tenho dúvidas que "
                          "vais amar o nosso CAPPUCCINO.\n"
                          "Uma dose de café para "
                          "bastante leite e espuma."
                          "Pode-se dizer que é a versão "
                          "italiana para a meia de leite.\n"
                          "Preferes um coração, uma "
                          "roseta ou um cisne?\n"
                          "Normalmente é no cappuccino "
                          "que nossos baristas se revelam grandes "
                          "artistas e praticam o LATTE-ART.")
                    alterar_dic("Cappuccino", "total_cl", dicionario)
                    good_or_bad("Cappuccino", dicionario)
            # Pequeno com leite -> Pingo.
            else:
                print("\nPodemos complicar e chamar de Macchiatto "
                      "ou podes ter a beira do balcão e"
                      " pedir um PINGO.\nUma dose de espresso na "
                      "chávena de espresso e leite cremoso.")
                alterar_dic("Pingo", "total_cl", dicionario)
                good_or_bad("Pingo", dicionario)
    # Sobrescrever o arquivo com os dados atualizados.
    with open("dicionario.txt", "w") as file:
        file.write(json.dumps(dicionario))
        file.close()

else:
    # Chamar a função para alterar os dados do dicionário.
    alterar_dic1("Acessos as estatisticas", dicionario)
    # Sobrescrever o arquivo com os dados atualizados.
    with open("dicionario.txt", "w") as file:
        file.write(json.dumps(dicionario))
        file.close()
    print("\nUm pouco sobre nossos clientes:\n",
          dicionario["total_cl"], " clientes já foram atendidos\n",
          dicionario["decididos"],
          " já sabiam o que escolher e "
          "não usaram nosso programa\n",
          dicionario["happy"],
          " Ficaram contentes com a recomendação\n",
          dicionario["sad"], " não gostaram da recomendação e "
                             "não compraram o café sugerido\n",

          # Porcentagem dos clientes que não quiseram usar o programa.
          "{0}%  dos clientes já sabiam o que".format(
              str(round((dicionario["decididos"] /
                         dicionario["total_cl"]) * 100))),
          "escolher e nao usaram o programa\n",
          # Porcentagem dos clientes felizes com a sugestão.
          "{0}%  dos clientes ficaram contentes com".format(
              str(round((dicionario["happy"] /
                         dicionario["total_cl"]) * 100))),
          "a recomendação\n")
    """Criar outro dicionário somente com dados dos cafés, 
    e não sobre os clientes."""
    new = {}
    for i in dicionario:
        if i == "V60" or i == "Espresso" or i == "Pingo" \
                or i == "Cappuccino" \
                or i == "Espresso duplo" or i == "Flat White":
            new[i] = dicionario[i]
    print("RESUMO DAS VENDAS \n"
          "(unidades/produto):")
    for i in new:
        print(new[i], "-", i)
    mais_vendido = max(new, key=new.get)
    menos_vendido = min(new, key=new.get)
    print("\nO café MAIS indicado foi o -> ", mais_vendido,
          " <- Com o total de", dicionario[mais_vendido],
          "sugestões.")
    print("O café MENOS indicado foi o -> ", menos_vendido,
          " <- Com o total de", dicionario[menos_vendido],
          "sugestões.\n\n")
    print("Já foram acessadas ",
          dicionario["Acessos as estatisticas"],
          "vezes os dados estatísticos")

    troca = input("Deseja alterar a palavra chave?\n "
                  "'S' para mudar ou 'N' para fechar o programa....")
    troca = troca.upper()
    while troca != "S" and troca != "N":
        print("\nCarregaste " + troca)
        troca = input("Carregue 'S' para trocar palavra passe ou, "
                      "'N' para terminar: ")
        troca = troca.upper()
    if troca == "S":
        nova = input("Digite a nova palavra passe "
                     "(mínimo 5 caracteres): ")
        confirma = input("Confirme a palavra passe: ")
        while nova != confirma or len(nova) < 5:
            if len(nova) < 5:
                print("A palavra passe escolhida não "
                      "possui ao menos 5 caracteres.\n")
            else:
                print("As palavras digitadas "
                      "não são correspondentes.\n")
            nova = input("Digite novamente a nova palavra passe "
                         "(mínimo 5 cracteres): ")
            confirma = input("Confirme a palavra passe: ")
        print("Palavra passe alterada com sucesso")
        # Sobrescrever o arquivo com a palavra passe atualizada.
        f = open("ps.txt", 'w')
        f.write(nova)
        f.close()
