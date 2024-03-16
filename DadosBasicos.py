nome = input("Digite seu nome:")
print("Bem vindo(a), seu nome é:",nome)
sexo = input("Digite seu sexo com M para masculino e F para feminino:")
if sexo.upper() == 'M':
  print("Sexo masculino.")
if sexo.upper() == 'F':
  print("Sexo feminino.")
dia = input("Qual seu dia de nascimento?")
mes = input("Qual seu mês de nascimento?")
ano = input("Qual seu ano de nascimento?")
print("Você nasceu no dia",dia,"de",mes,"de",ano)
idade = input("Qual sua idade?")
idade = int(idade)
if idade >= 18:
  print("Você é maior de idade.")
else:
  print("Você é menor de idade.")
altura = float(input("Qual sua altura?"))
peso = float(input("Qual seu peso?"))
imc = peso / (altura**2)
print("Seu IMC é:",imc)
print("Obrigado por usar nosso programa,",nome,"!Volte sempre!")