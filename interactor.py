# regula els torns, permet jugar partides amb normes a platform

import platform

class GameHandler():

	def __init__(self, playerset):

		self.__players = [ player for player,cl in playerset]
		self.__playerSet=playerset;
		self.game= platform.GameState(self.__players);

	def start(callback):
		stIn=self.indexOf(self.game.starter());
		sfp=self.__players;
		self.__players=sfp[stIn+1:]+sfp[:stIn+1]#mirar que fincione!!
		self.playerIndex=0;
		self.onEnd=callback;
		self.play()

	def play():
		player=self.__players[self.playerIndex]
		self.__playerset[player].play(self.game.gameHistory(), 
									  self.game.gameList(),
									  self.game.pieceList(player),
									  [p for p in self.__players],
									  game.nnum,
									  self.recieveGame)

	def recieveGame():
