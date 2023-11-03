key = int(input("Digite o número do exercício: "))

if key == 1:
  lista = [40, 50, 100]
  for i in lista:
    print(i)

if key == 2:
  limite = int(input("Informe o limite: "))
  lista = []
  for numeros in range(limite):
    lista.append(numeros + 1)

  print(lista)

if key == 3:
  limite = int(input("Informe o limite: "))
  lista = []
  for numeros in range(limite, 0, -1):
    lista.append(numeros)

  print(lista)

if key == 4:
  init = int(input("Digite o início: "))
  end = int(input("Digite o final: "))
  lista = []
  for numeros in range(init, end + 1):
    lista.append(numeros)
  print(lista)

if key == 5:
  init = int(input("Digite o início: "))
  end = int(input("Digite o final: "))
  lista = []
  for numeros in range(init, end + 1):
    lista.append(numeros)
    lista.sort(reverse=True)
  print(lista)

if key == 6:
  lista = []
  N = int(input("Informe a quantidade de dados na lista: "))
  c = 1
  for numeros in range(1, N + 1):
    numeros = int(input(f"Digite o dado número {c}: "))
    lista.append(numeros * 2)
    c += 1
  print(lista)
  '''
 # Eu havia feito isso antes esquecendo que eu tinha que OBRIGATÓRIAMENTE usar for e range:
	while c<=N:
		n = int(input(f"Digite o dado número {c}: "))
		lista.insert(c,n*2)
	'''
if key == 7:
  lista = []
  N = int(input("Digite o número para fazer a tabuada: "))
  for numeros in range(1, 11):
    lista.append(numeros * N)
  print(f"Tabuada do {N}: {lista}")

if key == 8:
  lista = []
  N = int(input("Digite o número de notas: "))
  c = 1
  for numeros in range(1, N + 1):
    numeros = int(input(f"Digite o valor da nota {c}: "))
    c += 1
    lista.append(numeros)
  print(f"Notas: {lista}")
  print(f"Média: {sum(lista)/N:.1f}")

if key == 9:
  par = []
  impar = []
  lista = []
  N = int(input("Digite o número de dados a serem digitados: "))
  c = 1
  for numeros in range(1, N + 1):
    numeros = int(input(f"Digite o {c}° número: "))
    if numeros % 2 != 0:
      impar.append(numeros)
      lista.append(numeros)
    elif numeros % 2 == 0:
      par.append(numeros)
      lista.append(numeros)
    else:
      print("Erro.")
    c += 1
  print(f"Números informados: {lista}")
  print(f"Números pares: {par}")
  print(f"Números ímpares: {impar}")

if key == 10:
  lista = []
  N = int(input("Digite o número de dados a serem digitados: "))
  c = 1
  mult = 1
  for numeros in range(1, N + 1):
    numeros = int(input(f"Digite o {c}° número: "))
    lista.append(numeros)
    c += 1
    mult *= numeros
  print(f"A lista é: {lista}")
  print(f"A soma é: {sum(lista)}")
  print(f"A multiplicação é: {mult}")

if key == 11:
  lista = []
  Nome = input("Digite o nome do(a) atleta: ")
  c = 1
  for numeros in range(1, 6):
    numeros = float(input(f"Digite a altura do salto {c} em metros: "))
    lista.append(numeros)
    c += 1
  print(f"Atleta: {Nome}")
  print(f"Saltos: {lista}")
  print(f"Média: {sum(lista)/5:.2f}m")
