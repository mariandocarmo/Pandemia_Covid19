def linha():
    print("="*35)

linha()
print("SEJA BEM VINDO!!")
linha()


print("Responda na seguinte questão com apenas (Sim) ou (Não)")
pergunta = input("Você conhece os principais sintomas do COVID-19? ")


if pergunta == "Sim":
    print("Você está no caminho certo! Use máscara e alcool em gel e só saia de casa se necessário!")
elif pergunta == "Não":
    print ("Saiba que estamos aqui para te informar mais sobre esta doença. \n\
    Passo Nº1: Use máscara e alcool em gel. \n\
    Passo Nº2: Mantenha o distanciamento social\n\
    para evitar a propagação do vírus")
    linha()
    print("Os principais sintomas do Covid 19 incluem --> \n\
    -Tosse, Febre, \n\
    coriza, Dor de garganta, Dificuldade para respirar, \n\
    Perda de olfato (anosmia), Alteração do paladar (ageusia), \n\
    Distúrbios gastrintestinais (náuseas/vômitos/diarreia), Cansaço (astenia), \n\
    Diminuição do apetite (hiporexia), Dispnéia ( falta de ar).")
else:
    print("Responda sim ou não. Tente novamente!")


linha()
print("Obrigado por participar do questionário!")
linha()

