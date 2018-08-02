from beautifultable import BeautifulTable

class Player:
	'''The details of each player are store in their own Player() object
	
	The player's attributes are referenced in the Game() object, but are
	updated/altered using the methods within this class.
	
	Attributes:
		name: A string that contains the player name.
		points: An integer that holds the player score.
		activeStatus: A boolean that indicates if the player is still in the game (has not been eliminated).
		calledYaniv: A boolean that indicates whether the player called Yaniv.
		calledAssaf: A boolean that indicates whether the player called Assaf.
	'''
	def __init__ (self):
		'''Inits Player with the starting state of all attributes.'''
		self.name = input("Enter the player's name: ")
		self.points = 0
		self.activeStatus = True
		self.calledYaniv = False
		self.calledAssaf = False

	def updatePlayerScore(self, pointsToBeAdded):
		'''Update the player's score using the points in hand at the end of the round. 
		The pointsToBeAdded are provided by a method call from the Game object, recordPlayerPoints().
		'''
		self.points += pointsToBeAdded

	def scoreExceedsMax(self, maxScore):
		'''Check to make sure that player's score is not greater than the limit set in the Game object.
		Eliminate the player if their score is too high using the eliminatePlayer() method.
		'''
		if self.points > maxScore:
			self.eliminatePlayer()

	def eliminatePlayer(self):
		'''Inform the player that he/she has been eliminated from the game and change their active status to reflect the elimination.'''
		print("Sorry {}... Your score is over {} so you've been eliminated.".format(self.name, game.maxScore))
		self.activeStatus = False
	
	def scoreIsMagicNum(self):
		'''If the player's score adds up to one of the magic numbers exactly, reduce their score by the reducer value.
		The magic numbers and the reducer are created at the beginning of the game as attributes in the Game object.
		'''
		if [True for nums in game.magicNums if self.points % nums == 0 and self.points != 0]:
			print("{}'s score was an even {} and will be reduced by {}.".format(self.name, self.points, game.magicReducer))
			self.points -= game.magicReducer		

class Game:
	'''All details pertaining to the game at hand are stored and modified using this Game object.
	
	This object contains methods that control the set up of the game (including adding players), the progress of the 
	game (rounds, point recording, showing scores), as well as the end of the game. All players created using the 
	Player() object are stored in an array within this Game object.
	
	Attributes:
		maxScore: A user-defined integer value that acts as the maximum score that a player can have without being eliminated.
		magicNums: An array of integers that represent the values that a player's score must be in order to get reduced (amount is magicReducer). 
		magicReducer: An integer by which a player's score can be reduced if it adds up to a specific value (given in magicNums).
		penaltyForBeingAssafed: An integer representing the value by which a player's score must be increased if another player 'Assafs' them.
		players: An empty array which will be filled with players in the addPlayers method.
		currentRound: An integer that acts as a counter to inform user of the current round being played.
	'''	
	def __init__(self):
		'''Inits Game with the starting state of all attributes.'''
		self.maxScore = int(input("What is the maximum amount of points a player can have? "))
		self.magicNums = [100, 150]
		self.magicReducer = 50
		self.penaltyForBeingAssafed = 30
		self.players = []
		self.currentRound = 0

	def addPlayers(self):
		'''Using the number of players given by user, create that many Player objects and add them to the players list.'''
		totalPlayers = int(input("Enter the number of players: "))
		
		for i in range(totalPlayers):
			self.players.append(Player())

	def playersInGame(self):
		'''Get the number of players that are still active (not eliminated) by subtracting the number of eliminated players (false active status in Player) 
		from the list of players. This value is used as a condition in main to determine when the game is over (only one player still active).
		'''
		numPlayers = len(self.players)
		
		for player in self.players:
			if player.activeStatus == False:
				numPlayers -= 1
			
		return numPlayers

	def roundResults(self):
		'''Perform tasks and checks that are done each round.
		Inform the user of the current round. Create a list of the players that have not yet been eliminated and use them for the remainder of the method.
		Check which player called Yaniv and whether any other player called Assaf. Then, depending on the situation (who Yaniv, Assaf y/n, points in hand),
		points are added to each active player's score. It is checked whether each player's score surpassed the max score, and whether the each player's score
		qualifies to be reduced by the magicReducer (if player score is one of the magicNums). Finally, a scoreboard is outputted to the user and the round ends.
		
		Function calls:
			printRoundMessage()
			whichPlayerCalledYaniv()
			anyPlayerCalledAssaf()
			self.recordPlayerPoints()
			updatePlayerScore() -- from Player object
			scoreExceedsMax() -- from Player object
			scoreIsMagicNum() -- from Player object
			showScoreboard()
		'''
		self.printRoundMessage()
		activePlayers = [player for player in self.players if player.activeStatus == True]
		self.whichPlayerCalledYaniv(activePlayers)
		self.anyPlayerCalledAssaf()
		
		for player in activePlayers:
			if player.calledYaniv == True:
				pointsFromRound = 0

				for potentialAssafer in self.players:
					if potentialAssafer.calledAssaf == True:
						pointsFromRound = self.recordPlayerPoints(player) + self.penaltyForBeingAssafed
	
			else:
				pointsFromRound = self.recordPlayerPoints(player)

			player.updatePlayerScore(pointsFromRound)
			player.scoreExceedsMax(self.maxScore) 
			player.scoreIsMagicNum()
		
		self.showScoreboard()

	def printRoundMessage(self):
		'''Output a stylized message informing the user what round it is currently.'''
		self.currentRound += 1
		print("-"*20, "Round {}".format(self.currentRound), "-"*20)

	def whichPlayerCalledYaniv(self, activePlayers):
		'''Ask the user which active player called Yaniv at the end of the round until they enter a valid option. 
		Handle when user enters an invalid option and remind to input an active user. Set the calledYaniv attribute to 'True' so that player doesn't accrue
		any points at the end of the round during roundResults() (unless a player calls Assaf*).
		'''
		foundYaniver = 0

		while foundYaniver == 0:
			yaniver = input("Which player called Yaniv? ")
			
			for player in activePlayers:
				if yaniver.lower() == player.name.lower():
					player.calledYaniv = True
					foundYaniver = 1

			if foundYaniver == 0:
				print("The player does not exist or has been eliminated.")
		
	def anyPlayerCalledAssaf(self):
		'''Check whether there was a player that called 'Assaf' at the end of the round. If there was an Assaf-er, get their name and set the calledAssaf attribute to 'True'.
		This is used during roundResults() to determine whether Yaniv-er gets Assafed or not.
		'''
		yesOrNoAssaf = ["no", "yes"]
		didAPlayerCallAssaf = ""
		foundAssafer = 0
		assafer = ""
		
		while didAPlayerCallAssaf not in yesOrNoAssaf:
			didAPlayerCallAssaf = input("Did a player call Assaf? (yes/no) ").lower()
			
		if didAPlayerCallAssaf == yesOrNoAssaf[1]:	
			while foundAssafer == 0:
				assafer = input("Which player called Assaf? ")
				
				for player in self.players:
					if assafer.lower() == player.name.lower():
						player.calledAssaf = True
						foundAssafer = 1			 
			
	def recordPlayerPoints(self, player):
		'''Get the number of points that were in the player's hand at the end of the round and return the value (called for each player from roundResults()).'''
		sumCards = int(input("How many points were in {}'s hand? ".format(player.name)))

		return sumCards	
	
	def showScoreboard(self):
		'''Create a table using the BeautifulTable module, which contains the player's names, as well as their scores and active status (eliminated or active) using
		the attribute information contained within each player object. Output this table to the user.
		'''
		table = BeautifulTable()
		table.column_headers = ["Name", "Score", "Status"]

		for player in self.players:
			playerStatus = "Active" if player.activeStatus else "Eliminated"
			table.append_row([player.name, player.points, playerStatus])

		print(table)

	def resetYanivAssafStatus(self):
		'''Reset all calledYanif and calledAssaf attributes of any relevant player in the player list to false to prepare for the next round.'''		
		for player in self.players:
			if player.calledYaniv == True:
				player.calledYaniv = False
				 
			if player.calledAssaf == True:
				player.calledAssaf = False 	
			
	def theWinnerIs(self):
		'''Outputs a message congratulating the winner (only player in the list with an active status).'''
		for player in self.players:
			if player.activeStatus == True:
				winner = player.name
			
		print("Congratulations {}, you won the game!".format(winner))

game = Game()
game.addPlayers()

# Collect the results of each round while there are still more than one players that are still in the game.
while game.playersInGame() > 1:
	game.roundResults()
	game.resetYanivAssafStatus()

game.theWinnerIs()

print("Good game everyone")			
