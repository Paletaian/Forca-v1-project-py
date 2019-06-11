

# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)


# Classe
class Hangman() :

	# Método Construtor
	def __init__(self, word) :
		self.board = ['''
>>>>>>>>>>Hangman<<<<<<<<<<
+---+                                                                                                                                                                                           
|   |                                                                                                                                                                                           
|                                                                                                                                                                                               
|                                                                                                                                                                                               
|                                                                                                                                                                                               
|                                                                                                                                                                                               
=========''', '''

+---+
|   |                                                                                                                                                                                          
|   O                                                                                                                                                                                          
|                                                                                                                                                                                              
|                                                                                                                                                                                              
|                                                                                                                                                                                              
=========''', '''

+---+                                                                                                                                                                                          
|   |                                                                                                                                                                                          
|   O                                                                                                                                                                                          
|   |                                                                                                                                                                                          
|                                                                                                                                                                                              
|                                                                                                                                                                                              
=========''', '''

+---+                                                                                                                                                                                          
|   |                                                                                                                                                                                          
|   O                                                                                                                                                                                          
|  /|                                                                                                                                                                                          
|                                                                                                                                                                                              
|                                                                                                                                                                                              
=========''', '''

+---+
|   |
|   0
|  /|\                                                                                                                                                                                         
|                                                                                                                                                                                              
|                                                                                                                                                                                              
=========''', '''

+---+
|   |
|   O
|  /|\                                                                                                                                                                                         
|  /                                                                                                                                                                                           
|                                                                                                                                                                                              
=========''', '''

+---+
|   |
|   O
|  /|\                                                                                                                                                                                         
|  / \                                                                                                                                                                                         
|                                                                                                                                                                                              
=========''']
		li = []
		for i in word:
			li.append(i)
		self.word1 = word
		self.word2 = ['=' for lil in word]
		self.word = li
		self.loser = []
		self.winner = []
		self.counter = 0
		ini = len(word)
		self.tim = 0
		self.word3 = self.word
		self.wordc = self.word2[::1]
		self.wordalt = self.word
	# Método para adivinhar a letra
	def guess(self, a):
		xol = self.wordalt
		self.a = a
		if1 = len(xol) + 1
		for i in xol:
			if i == a:
				self.winner.append(a)
			else:
				if1 = if1 - 1
		try:
			for im in self.wordalt:
				self.wordalt.remove(a)
		except:
			pass
		if if1 == 1:
			self.loser.append(a)
		self.if1 = if1

# Método para verificar se o jogo terminou
	def hangman_over(self):
		jol = len(self.loser)
		lol = len(self.board)
		if jol == lol:
			return True
		else:
			return False


# Método para verificar se o jogador venceu
	def hangman_won(self):
		world = len(self.wordalt)
		if world == 0:
			return True
		else:
			return False


# Método para não mostrar a letra no board
	def hide_word(self):
		self.time = 0
		boardword = ''
		try:
			for intc in self.word3:
				self.word3.remove(self.a)
				self.time = self.time + 1
		except :
			pass
		for inn in range(self.time):
			self.wordc.remove('=')
			self.word2 = self.wordc
			xlo = self.word1.index(self.a) + inn
			self.word2.insert(xlo, self.a)
			self.word1.remove(self.a)
		for ilolil in range(len(self.word2) + 1) :
			if ilolil % 2 == 1 :
				self.word2.insert(ilolil, ' ')
			else:
				pass
		return self.word2


# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self, boardword):
		try:
			if self.time == 0:
				pass
			else:
				pass
			de2 = " " + filter(lambda a, b: a+b, boardword)
		except:
			de2 = " " + '= ' * len(self.word1)
		board = self.board
		print(board[len(self.loser)], de2)
		print("\nAcertos:")
		for item in self.winner:
			print(item)
		print("\nErros:")
		for itens in self.loser:
			print(itens)

palavras = ["amigo", "beterraba", "dia", "noite", "ademais", "domador", "assasino", "alcaçus", "salamandra"]

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word(palavras):
	import ianpack
	esc = ianpack.random(len(palavras), 1)
	return palavras[esc[0]]
# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
game = Hangman(rand_word(palavras))
y = 0
while True:
	if y == 0:
		game.print_game_status(0)
	else:
		game.print_game_status(game.hide_word())
	inp1 = input('\nTentativas: ')
	inp = inp1[0].lower()
	game.guess(inp)
	y = 1

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print('\nParabéns! Você venceu!!')
		print("\nFoi bom jogar com você! Agora vá estudar!\n")
		break
	elif game.hangman_over():
		print('\nGame over! Você perdeu.')
		print('A palavra era ' + game.word1)
		print("\nFoi bom jogar com você! Agora vá estudar!\n")
		break
	else:
		pass
