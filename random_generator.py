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
gh = interactor.GameHandler({'1': p1, '2': p2})
a=gh.start();

st=time.time();
for i in range(10000):
	gh.restart()
	if not i % 100:
		print i/100;

ed=time.time();

print ed-st;