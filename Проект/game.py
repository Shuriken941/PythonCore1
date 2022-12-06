from __future__ import print_function
import random
import boards
from sys import argv



def importwordlist(file):
	with open(file, 'r', encoding='utf-8') as f:
		words = list(filter(None, f.read().split('\n')))
		return words

class gameboard(object):

	def __init__(self, difficulty, wordlist):
		self.difficulty = difficulty
		self.words = wordlist
		hangmanpics = ''

	def choosedifficulty(self, difficulty):
		if self.difficulty == "легка":
			hangmanpics = boards.easy
			return hangmanpics

		elif self.difficulty == "важка":
			hangmanpics = boards.hard
			return hangmanpics
	
	def displaygameboard(self, hangmanpics, missedLetters, correctLetters, secretWord):
		print(hangmanpics[len(missedLetters)])
		print()
		
		print("Не правильні букви: ", end=' ')
		for letter in missedLetters:
			print(letter, end = ' ')
		print()
		
		blanks = '_' * len(secretWord)
		
		for i in range(len(secretWord)):
			if secretWord[i] in correctLetters:
				blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
			
		for letter in blanks:
			print(letter, end=' ')
		
		print()

	
class GameEngine(object):
	def __init__(self, board):
		self.gameboard = board
		self.missedLetters = ''
		self.correctLetters = ''
		self.gameisdone = False
	
	def getRandomWord(self, wordList):
		wordindex = random.randint(0, len(wordList)-1)
		return wordList[wordindex]
	
	def getGuess(self, alreadyGuessed):
		while True:
			print('Введіть букву:')
			guess = input('> ').lower()
			if len(guess) != 1:
				print("Будь ласка, введіть лише одну букву")
			elif guess in alreadyGuessed:
				print("Ви вже вибирали таку букву, введіть іншу")
			elif guess not in 'йцукенгшщзхїфівґапролджєячсмитьбю':
				print("Не обманюй, це не буква:)")
			else:
				return guess
	
	def playagain(self):
		print('Хочете розпочати гру знову? Введіть будь ласка так чи ні')
		return input('> ').lower().startswith('т')
	
	def oneguess(self, secretWord):

		self.hangmanpics = self.gameboard.choosedifficulty(self.gameboard.difficulty)
		self.gameboard.displaygameboard(self.hangmanpics, self.missedLetters, self.correctLetters, secretWord)
		guess = self.getGuess(self.missedLetters + self.correctLetters)
		if guess in secretWord:
			self.correctLetters = self.correctLetters + guess
			
			foundAllLetters = True
			for i in range(len(secretWord)):
				if secretWord[i] not in self.correctLetters:
					foundAllLetters = False
					break
			if foundAllLetters:
				print("Вітаю, правильне слово %s! Кількість непривильних букв %d." %(secretWord, len(self.missedLetters)))
				self.gameisdone = True
		else:
			self.missedLetters = self.missedLetters + guess
			if len(self.missedLetters) >= len(self.hangmanpics) - 1:
				self.gameboard.displaygameboard(self.hangmanpics, self.missedLetters, self.correctLetters, secretWord)
				print("Шкода, але ти вичерпав кількість спроб! Кількість правильних відповідей %d ,а не правильних %d. До речі, правильне слово %s." %(len(self.correctLetters), len(self.missedLetters), secretWord))
				self.gameisdone = True
		
		
				
class game(object):
	def __init__(self, mygame):
		self.mygame = mygame
	
	def play(self):
		secretWord = self.mygame.getRandomWord(words)
		while True:
			self.mygame.oneguess(secretWord)
			if self.mygame.gameisdone:
				if self.mygame.playagain():
					secretWord = self.mygame.getRandomWord(words)
					self.mygame.missedLetters = ''
					self.mygame.correctLetters = ''
					self.mygame.gameisdone = False
				else:
					quit()
	
				
if __name__ == '__main__':
	try:
		script, difficulty = argv
	except(ValueError):
		print("Будь ласка, вибери для початку важкість, легка чи важка:")
		difficulty = input("> ")
	words = importwordlist('wordlist.txt')
	myboard = gameboard(difficulty.lower(), words)
	mygame = GameEngine(myboard)
	play = game(mygame)
	play.play()
