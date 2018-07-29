from beautifultable import BeautifulTable

#### CLASS ####


class Player:
	def __init__(self, name):
		self.name = name

	def setupPlayer(self):
		self.points = 0

	def endRoundPoints(self):
		MAXSCORE = 200
		MAGICNUMS = [100, 150]
		# get points from end of round
		sumCards = int(
		    input("How many points did {} finish with? ".format(self.name)))
		self.points += sumCards  # add it to current score
		if self.points > MAXSCORE:  # check if player lost
			print("Sorry {}, your score is {}...\nYou're out of the game!".format(
			    self.name, self.points))
			return -99
		# or if the player's score matches one of the magic numbers'
		elif [True for nums in MAGICNUMS if self.points % nums == 0]:
			self.magicNumber()

	def magicNumber(self):
		MAGICREDUCER = 50
		print("Sweet moves {}! Your points are an even {}, and will get reduced by {}!".format(
		    self.name, self.points, MAGICREDUCER))
		self.points -= MAGICREDUCER  # reduce score by 50 if hit magic number

#### FUNCTIONS ####


def createPlayer():
	playerName = input("Player name: ")
	return Player(playerName)


def createPlayers(numPlayers):
	playerList = []
	for i in range(numPlayers):
		player = createPlayer()
		player.setupPlayer()
		playerList.append(player)
	return playerList


def styleRounds(round):
	# informs players of the current round and separates current from previous
	print("-" * 20, "Round {}".format(round), "-" * 20)


def showScoreboard(players):  # creates a schweet-looking table to show everyone's points'
	table = BeautifulTable()
	table.column_headers = ["name", "score"]

	for people in players:
		table.append_row([people.name, people.points])
	print(table)


def playRound(players, round):
	styleRounds(round)

	losingPlayers = []

	# Record the score of all players. Remove the player from the list if they pass the max score.
	for player in playerList:
		# people.recordPoints()
		# people.points = getUserInput("How many points?")
		# if people.passedMaxScore():
		#  people.printLosingMessage()
		#	losingPlayers.append(people)

		# Record points for the end of the round.Check if person lost as well as record score -- if lose, print losing message
		# -99 is a special value returned when the player has exceeded the max score
		# people.recordPoints()
		# if people.score > 200:
		# 	losingPlayers.append(people)

		# Record points for the end of the round.Check if person lost as well -- if lose, print losing message
		player.recordScore()
		if player.exceedsMaxScore():
			losingPlayers.append(player)
		

		#if people.endRoundPoints() == -99: 
			#add the losing player to the list to be removed
			#losingPlayers.append(people)

	# Remove the losing players from the original player list
	for losers in losingPlayers:
		players.remove(losers)

	showScoreboard(players)					
