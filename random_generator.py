import random as rnd;
import time;
import interactor;

class RG:
	def __init__(self):
		pass;

	def play(self,pieces=None, 
			history=None, 
			game=None, 
			players=None, 
			nnum=None,
			remainingPieces=None,
			canPlay=None,
			callback=None):
		for piece in pieces:
			for i in range(2):
				if canPlay(piece, i):
					callback(piece,i);
					return;
		print "lel"

p1=RG()
p2=RG()
gh = interactor.GameHandler({1: p1, 2: p2})
a=gh.start();

st=time.time();

def cleaner(game):
	played=[ k.piece.end()  if k.end==1 else k.piece.start() for k in game['history'] if k.action=='play'];
	played+=[-1]*(28-len(played))
	end=[                   k.end                         for k in game['history'] if k.action=='play'];
	end+=[-1]*(28-len(end))
	drawn=[0]*28;
	for k in game['history']:
		if k.action=='draw':
			drawn[k.turn]=k.piece
	return [played, end, drawn, game['winner']];

data=[cleaner(gh.restart()) for i in range(100)]

ed=time.time();

print ed-st;