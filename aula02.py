contador = 0
while contador < 10:
    variavel = input("Digite um número: ")
    if variavel == "1":
        print(f"O valor digitado foi {variavel}, porém o valor impresso é 100")
        contador +=1
        continue
    elif variavel == "2":
        print(f"O valor digitado foi {variavel}, porém o valor impresso é 200")
        contador +=1
        continue
    elif variavel == "3":
        print(f"O valor digitado foi {variavel}, porém o valor impresso é 300")
        contador +=1
        continue
    elif variavel == "4":
        print(f"O valor digitado foi {variavel}, porém o valor impresso é 400")
        contador +=1
        continue
    elif variavel == "5":
        print(f"O valor digitado foi {variavel}, porém o valor impresso é 500")
        contador +=1
        continue
    else: 
        print(f"O valor digitado foi {variavel}, porém o valor impresso é 1000")
        contador +=1
        continue
print(f"A quantidade de vezes que foi teclado um número foi: {contador} ")
