#Email: alvaro.magnum@ifpb.edu.br

# Crie um programa em Python que é um cadastro de pessoas: - pedir um numero ao usuario


pessoas = int(input("Digite o número de pessoas: "))

listaNomes = []
listaIdades = []
listaCPF = []


for i in range(pessoas):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    cpf = int(input("Digite o CPF da pessoa: "))

    listaNomes.append(nome)
    listaIdades.append(idade)
    listaCPF.append(cpf)

pesquisa = input("Pesquise a pessoa pelo nome:")

for nome in listaNomes:
    if pesquisa == listaNomes[listaNomes.index(nome)]:
        print(f"A nome da pessoa é: {listaNomes[listaNomes.index(nome)]}")
        print(f"A idade da pessoa é: {listaIdades[listaNomes.index(nome)]}")
        print(f"O CPF da pessoa é: {listaCPF[listaNomes.index(nome)]}")





