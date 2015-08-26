import random as rnd;

N_NUMBERS=7; #numbers from 0 to 6

class CheatError (Exception):
        def __init__(self, player, value):
            self.value = value
        def __str__(self):
            return repr(self.value)


class Piece():
    def __init__(self, i,j):
        self.__start=i;
        self.__end=j;
        self.__min=min(i,j);
        self.__max=max(i,j);
        self.__pwd=rnd.random();

    def reverse(self):
        self.__start, self.__end=self.__end, self.__start

    def end(self):
        return self.__end;

    def start(self):
        return self.__start;

    def min(self):
        return self.__min;

    def max(self):
        return self.__max;

    def __repr__(self):
        return ('['+str(self.__start)+'|'+str(self.__end)+']')

def pieceDeck():
    return [Piece(i,j) for i in range(N_NUMBERS) for j in range(i+1)]


class GameState():
    def __init__(self, players):
        self.__players=players; #guardar jugadors
        self.__originalpieces=pieceDeck() #crear fitxes
        self.__randState=rnd.getstate(); #guardar estat del generador aleatori
        self.__pieces=[piece for piece in self.__originalpieces] #copiar el vector de peces
        rnd.shuffle(self.__pieces);  #barrejar la còpia (nota, tot i que l'ordre sigui diferent, les peces son les mateixes (es passen per referència))
        self.__decks={player:[self.__pieces.pop() 
                        for piece in range(N_NUMBERS)] 
                            for player in players}; #dona a cada jugador 7 peces de les desordenades, i les treu de __pieces.
        self.__gameList=[]; #should we make it a collections.deque?
        self.__gameHistory=[];
        self.__turn=0; #cada jugador fa un torn! (no una ronda sencera) (modul jugadors)

    def play(self, player, piece, end, byPass=False):

        empty= len(self.__gameList)==0

        if not empty and not byPass: #si fas el byPass=True no comprova que no facis trampes (util per fer entrenaments quan saps que funciona)
            self.canPlay(player, piece, end, error=True);

        if end == 1:
            if not empty and self.__gameList[-1].end()==piece.end():
                piece.reverse()
            self.__gameList.append(piece);
            self.__gameHistory.append(GameAction('play', piece, self.__turn, end)); #falta programar
            self.__decks[player].remove(piece);

        elif end == 0:
            if not empty and self.__gameList[0].start()==piece.start():
                piece.reverse()
            self.__gameList.insert(0, piece)
            self.__gameHistory.append(GameAction('play', piece, self.__turn, end));
            self.__decks[player].remove(piece);


        else:
            raise CheatError(player, "Unknown end!");
        self.__turn+=1;

    def canPlay(self, player, piece, end, error=False): #comprova que no hi ha trampes!

        if error:
            if not piece in self.__originalpieces:
                raise CheatError(player,'Unknown Piece');
            if piece in self.__gameList:
                raise CheatError(player,'Piece Already Played');
            if not piece in self.__decks[player]:
                raise CheatError(player+'Piece not of own property played');
            if (end == 1 and 
                not (   self.__gameList[-1].end() == piece.end() 
                     or self.__gameList[-1].end() == piece.start()) ):
                raise CheatError(player,'Incorrect Piece');
            if (end == 0 and 
                not (   self.__gameList[0].start() == piece.end() 
                     or self.__gameList[0].start() == piece.start()) ):
                raise CheatError(player,'Incorrect Piece');
        else:

            if not piece in self.__originalpieces:
                return False;
            if piece in self.__gameList:
                return False;
            if not piece in self.__decks[player]:
                return False;
            if (end == 1 and 
                not (   self.__gameList[-1].end() == piece.end() 
                     or self.__gameList[-1].end() == piece.start()) ):
                return False;
            if (end == 0 and 
                not (   self.__gameList[0].start() == piece.end() 
                     or self.__gameList[0].start() == piece.start()) ):
                return False;
        return True;


    def draw(self, player, byPass=False):
        n=0;
        while True:
            if not self.canDraw(player):
                self.gameHistory.append(GameAction(action='draw', pieces=n, player=player, turn=self.__turn));
                return True;
            if len(self.__pieces)==0:
                return False;
            piece=self.__pieces.pop()
            self.__decks(player).append(piece);
            n+=1;

    def canDraw(player):
        for piece in self.__decks[player]:
            for end in range(2):
                if self.canPlay(player,piece, end):
                    return False;
        return True; 

    def pieceList(self,player):
        return [piece for piece in self.__decks[player]];

    def starter(self):
        k=(N_NUMBERS*(N_NUMBERS+1))/2;
        for c in range( k ):
            piece=self.__originalpieces[k-c-1];
            for player in self.__players:
                if piece in self.__decks[player]:
                    self.play(player, piece, 1);
                    return player;

    def players(self):
        return [player for player in self.__players];

    def isEnded(self):
        for player in self.__players:
            if len(self.__decks[player])==0:
                return player;
        if not N_NUMBERS%2:
            print "The number is not odd, you'll have problems (saturacio)!";
        a = self.__gameList[0].start(); 
        z = self.__gameList[-1].end();

        if a !=z:
            return False;
        #mirar si satura
        cont = 0;
        for piece in self.__gameList:
            if piece.start() == a or piece.end() == a:
                cont+=1;
        if cont != N_NUMBERS:
            return False;

        totalsum = 0;
        winner=None;

        for player in self.__players:
            partialsum=0;
            for piece in self.__decks[player]:
                partialsum += piece.start() + piece.end();
            if partialsum>= totalsum:
                totalsum = partialsum;
                winner=player;

        return winner;





class GameAction():
    def __init__(self, action=None, pieces=None, player=None, turn=None, end=None):
        self.action=action;
        self.pieces=pieces;
        self.player=player;
        self.turn=turn;
        self.end=end;

    def __repr__(self):
        return ('['+str(self.action)+'|'+str(self.action)+']')

