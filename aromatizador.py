from collections import namedtuple
import shelve

menu = '''
======================================================
Gerenciador de cadastro de Aromatizantes de Ambiente
======================================================

1 - Adicionar Aromatizador
2 - Pesquisar Aromatizador
3 - Excluir Aromatizador
4 - Listar Aromatizador
5 - Sair


Digite uma opção: '''

aroma = shelve.open("aroma.db")
Aromatizador = namedtuple("Aromatizador", "nome essencia milimetros cor")
aromatizantes_tabela = "\n{:<3}{:<15}{:^10}{:^15}{:^15}".format("Aromatizante", "Nome", "Essência", "Milímetros", "Cor")

def adicionarAromatizador():
	nome = input("\nDigite o nome do Aromatizador: ")
	if nome in aroma.keys():
		print("\nAromatizador já cadastrado.")
		return

	essencia = input("Digite a essência do Aromatizador: ")#Essência do Aromatizador
	milimetros = input("Digite quantos milímetros você deseja: ")#Milímetros do Aromatizador
	cor = input("Digite sua cor: ")#Qual será a cor
	aroma [nome] = Aromatizador(nome, essencia, milimetros, cor)
	print("\nAromatizador cadastrado com sucesso!")


def pesquisarAromatizador():
	if not aroma:  # Se a lista não obter aromatizador
		print("\nNão há aromatizador cadastrado.")

	else:
		pesquisarAromatizador = input("\nNome do Aromatizador: ")

		for Aromatizador, key in enumerate(aroma.keys()):
			if aroma[key].nome == pesquisarAromatizador:
				print(aromatizantes_tabela)
				imprimirAromatizador(Aromatizador, aroma[key])
				return

		print("\nAromatizador não encontrado.")


def excluirAromatizador():
	if listarAromatizadores():
		try:
			aromatizador_excluir = int(input("\nAromatizante do aromatizante para excluir: "))
			if aromatizador_excluir <= 0 or aromatizador_excluir > len(aroma):
				print("\nAromatizante não existe no cadastro!")
		except:
			print("\nEntrada inválida!")
			return

		for Aromatizador, key in enumerate(aroma.keys()):
			if Aromatizador == aromatizador_excluir - 1:
				del aroma[key]
				print("\nAromatizador excluído com sucesso! ")


def listarAromatizadores():
	if not aroma:  # Se a lista nao obtém aromatizante
		print("\nNão há aromatizador cadastrado.")
		return False

	else:
		print("{:=^70}".format("Aromatizantes cadastrados"))
		print(aromatizantes_tabela)
		for Aromatizador, key in enumerate(aroma.keys()):
			imprimirAromatizador(Aromatizador, aroma[key])

		return True

def imprimirAromatizador(Aromatizante, Aromatizador):
        print("{:<3}{:<15}{:^10}{:^15}{:^15}".format(Aromatizante + 1,
	Aromatizador.nome,
	Aromatizador.essencia,
	Aromatizador.milimetros,
	Aromatizador.cor))


while True:
	try:
		op = int(input(menu))
	except:
		print("\nENTRADA INVÁLIDA!")
		continue

	if op == 5:
		aroma.close()
		break
	elif op == 1:
		adicionarAromatizador()
	elif op == 2:
		pesquisarAromatizador()
	elif op == 3:
		excluirAromatizador()
	elif op == 4:
		listarAromatizadores()
	else:
		print("\nOPÇÃO INVALIDA!")
exit()
