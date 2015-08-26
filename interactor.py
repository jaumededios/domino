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
		self.__players=sfp[stIn:]+sfp[:stIn]#mirar que fincione!!
		