print("=======================================")
print("|         CALCULADORA DE IMC          |")
print("|         CALCULADORA DE IMC          |")
print("|         CALCULADORA DE IMC          |")
print("=======================================")

print("\n")
print("Calcule seu IMC!")
print("\n")

peso = float(input("Digite o seu peso:"))
print("Peso coletado")
print("\n")

altura = float(input("Digite sua altura (exmeplo 1.70):"))
print("Altura coletado!")
print("\n")

imc = peso / (altura ** 2)
print("O seu IMC é {:.1f}".format(imc))


if imc <= 18.5:
    grupo = 'Magreza'
elif 18.6 <= imc < 24.9:
    grupo = 'Normal'
elif 25.0 <= imc < 29.9:
    grupo = 'Sobrepeso'
elif 30.0 <= imc < 30.9:
    grupo = 'Obesidade'
else:
    grupo = 'Obesidade Grave'

########################################################################


print("Gostaria de saber em qual grupo você se enquadra?")

while True:
    resposta=input("Digite sim ou não:")
    
    if resposta == 'sim':
        print(f"O seu grupo é {grupo}")
        break
    elif resposta == 'não':
        print("Ok, finalizando!")
        break
    elif resposta == 'nao':
        print("Ok, finalizando!")
        break
    elif resposta == 'NÃO':
        print("Ok, finalizando!")
        break
    elif resposta == 'NAO':
        print("Ok, finalizando!")
        break
    else:
        print("Desculpe, não entendi a resposta. Por favor, responda com 'sim' ou 'não'.")
        
