from yanivScorekeeper import yaniv_scorekeeper

def main():
	playerList = []
	round = 0
	totalPlayers = int(input("How many players: ")) #get max range
    game = yaniv_scorekeeper.Yaniv(totalPlayers)
    game.start()

	playerList = yaniv_scorekeeper.createPlayers(totalPlayers)
			
	while len(playerList) > 1:
		round += 1
		yaniv_scorekeeper.playRound(playerList, round)

	print("Congratulations {}! You won the game!".format(playerList[0].name))

if __name__ == "__main__":
	main()