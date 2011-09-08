from collections import defaultdict
"""
This module is for keeping track of scores in games of any number of players.
"""
players = set()
scoredict = defaultdict(int)


def addPlayer(p): #p should be a string name of the player
	players.add(p)

def removePlayer(p):
	if p in players:
		players.remove(p)

def clear():
	players.clear()
	scoredict = defaultdict(int)
	
def highestScore():
	if not len(scores): return 0
	return max(scores.keys())
	
def winning(p):
	return scores[p] is highestScore()
	
def winningPlayers():
	return [p for p in players if scores[p] is max(scores.values())]
	
def award(p, points=1):
	scores[p] += points

