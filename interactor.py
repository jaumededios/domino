# regula els torns, permet jugar partides amb normes a platform

import platform
import random as rnd;

class GameHandler():

	def __init__(self, playerset,callback=None):
		self.__players = [ player for player in playerset]
		self.__playerSet=playerset;
		self.game= platform.GameState(self.__players);
		self.callback=callback;
		self.toReturn=None;

	def restart(self):
		self.game= platform.GameState(self.__players);
		return self.start()


	def start(self):
		stIn=self.__players.index(self.game.starter());
		sfp=self.__players;
		self.__players=sfp[stIn+1:]+sfp[:stIn+1]#mirar que fincione!!
		self.playerIndex=0;
		self.play()
		return self.toReturn;

	def play(self ):
		self.player=self.__players[self.playerIndex];
		#what the line below means if the process of 
		#drawing pieces untill you can play (it may as well be 
		#drawing O pieces), ended in an error.
		if not self.game.draw(self.player): #this line is DEFINITELY NOT idiomatic and should be killed with fire
			self.playerIndex=(self.playerIndex+1)%len(self.__players);
			return self.play();
		player=self.player
		self.__playerSet[player].play(pieces=self.game.pieceList(player),#piezas
									  history=self.game.gameHistory(), #historial
									  game=self.game.gameList(), #partida
									  players=[p for p in self.__players], #lista de jugadores
									  nnum=self.game.nnum, #numero de piezas
									  remainingPieces=self.game.remainingPieces(),
									  canPlay= (lambda x,y: self.game.canPlay(self.player,x,y)),
									  callback=self.recieveGame)

	def recieveGame(self, piece=None, end=None):
		#print self.game.pieceList(self.player);
		self.game.play(self.player,piece,end);
		a=self.game.isEnded();
		#print "User "+self.player+" played "+str(piece)

		if a!=False:
			#print "The end is here!  \n"
			#print self.game.gameList();
			#print "\n_______________________________________"
			if(self.callback):
				self.callback(
					pieces={p:self.game.pieceList(p) for p in self.__players},
					history=self.game.gameHistory(), #historial
					game=self.game.gameList(), #partida
					players=[p for p in self.__players], #lista de jugadores
					nnum=self.game.nnum, #numero de piezas
					remainingPieces=self.game.remainingPieces())
			else: 
				self.toReturn={
					"pieces": {p:self.game.pieceList(p) for p in self.__players},
					"history": self.game.gameHistory(), #historial
					"game": self.game.gameList(), #partida
					"players": [p for p in self.__players], #lista de jugadores
					"nnum": self.game.nnum, #numero de piezas
					"remainingPieces": self.game.remainingPieces()
				}
			return a;

		self.playerIndex =(self.playerIndex+1)%len(self.__players);
		if self.playerIndex==0 and False:
			print ""
			print self.game.gameList();
			print "\n_______________________________________"
		self.play();
