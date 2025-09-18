nome = "Walmir Lima"
idade = 18;
telefone = "99946-9429"
cep = "58398-000"
isEstudante = True
texto = """Esse texto pode ter várias linhas"""

print("Hello World!")
print(nome)
print(idade)
print(cep)
print(isEstudante)
print(texto)

#Crie um programa que guarda os seguintes dados em variéveis:

#Nome da pessoa, endereço completo (rua, cep, número, complemento, bairro, cidade),
#se a pessoa é maior de idade, data de nascimento, altura e tipo sanguíneo.

print("\n------------------------- Resolução --------------------------\n")

nomeDaPessoa = "Walmir Lima"

rua = "Antônio Clementino dos Santos"
cep = "58398-000"
complemento = "Casa verde"
bairro = "Padre Cícero"
cidade = "Remígio"

dataDeNascimento = "24/10/2006"
indicesData = dataDeNascimento.split('/')
anoNascimento = int(indicesData[2])
ehMaiorDeIdade = anoNascimento >= 18

idade = 2025 - anoNascimento

altura = "1.80"
tipoSanguineo = "A+"

print("Nome:", nomeDaPessoa, "\n", "Rua:", rua, "\n", "Cep:", cep, "\n", "Complemento:", complemento, "Bairro:", bairro, "Cidade:", cidade, "\n", "Idade:", idade, "\n", "É maior de idade:", "\n", ehMaiorDeIdade, "Data de nascimento", dataDeNascimento, "\n", "Altura:", altura, "\n", "Tipo sanguíneo:", tipoSanguineo, "\n")

#Teste de lista de conjustos:

sequencia = str(input("Digite a lista de números: "))

numeros = sequencia.split(" ")

print(numeros)

lista = []

for numero in numeros:
    print(numero)
    lista.append(int(numero))

print(lista) #Lista final

