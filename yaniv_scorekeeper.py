from beautifultable import BeautifulTable

#### CLASS ####

class Player:
	
	def __init__ (self, name):
		self.name = name
	
	def setupPlayer(self):
		self.points = 0

	def endRoundPoints(self):		
		MAXSCORE = 200
		MAGICNUMS = [100, 150]
		
		sumCards = int(input("How many points did {} finish with? ".format(self.name))) #get points from end of round
		self.points += sumCards  #add it to current score

		if self.points > MAXSCORE: #check if player lost
			print("Sorry {}, your score is {}...\nYou're out of the game!".format(self.name, self.points))
			return -99
		elif [True for nums in MAGICNUMS if self.points % nums == 0]: #or if the player's score matches one of the magic numbers'
			self.magicNumber()

	def magicNumber(self):		
		MAGICREDUCER = 50
		
		print("Sweet moves {}! Your points are an even {}, and will get reduced by {}!".format(self.name, self.points, MAGICREDUCER))
		self.points -= MAGICREDUCER #reduce score by 50 if hit magic number

#### FUNCTIONS ####
				
def createPlayer():
	playerName = input("Player name: ")
	return playerName

def addPlayers(players):
	totalPlayers = int(input("How many players: ")) #get max range
	
	for i in range(totalPlayers):
		playerO = Player(createPlayer()) #make player object with name given from createPlayer fxn
		playerO.setupPlayer() #use class to setup player with points		
		players.append(playerO) #add object to the player list

def styleRounds(round):
	print("-"*20,"Round {}".format(round),"-"*20) #informs players of the current round and separates current from previous

def showScoreboard(players): #creates a schweet-looking table to show everyone's points'
	table = BeautifulTable()
	table.column_headers = ["name", "score"]
	
	for people in players:
		table.append_row([people.name, people.points])	
	print(table)	
		
def playRound(players, round):
	styleRounds(round)
	
	for people in players:		
		if people.endRoundPoints() == -99: 
			players.remove(people) #remove player from game if their points at the end of the round are higher than what is set

	showScoreboard(players)					

#### MAIN ####

playerList = []
round = 0
		
addPlayers(playerList)

while len(playerList) > 1:
	round += 1
	playRound(playerList, round)

print("Congratulations {}! You won the game!".format(playerList[0].name))