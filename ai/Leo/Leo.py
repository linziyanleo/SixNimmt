#!/usr/bin/env python
import sys
import random
import logging
import os
class AI:
    def __init__(self):
        self.name = ''
        self.cards = []
        self.logFileName = os.path.join(os.path.dirname(__file__), 'log')
        logging.basicConfig(filename = self.logFileName, level=logging.INFO)
    def InfoSetup(self, setupData):
        pass
    def InfoNewGame(self, newGamedata):
        self.cards = newGamedata[:]
        pass
    def InfoGame(self, gameData):
		self.cards = gameData #from the help of master siyao
        pass
    def InfoMove(self, cardData):
        pass
    def InfoScore(self, scoreData):
        pass
    def InfoGameEnd(self, gameEndData):
        pass
    def CmdPickCard(self):
        self.cards.sort()
		row = self.infoGame["rows"]
		for i in self.cards:
			if i < row[0][0]:
				
			for n in range(4):
				if 
				pri = abs(row[n][-1]-i)
				

        return self.cards.pop()

	#from the help of master Acc404
	def Xscore(self,data):
		sumRow = []
		for i in range(4):
			rowData = data[i]
			rowScore = 0
			for n in rowData:
				if i == 55:
					rowScore += 7
				elif n%11 == 0:
					rowScore += 5
				elif n%10 ++ 0:
					rowScore += 3
				elif n%5 == 0:
					rowScore += 2
				else:
					rowScore += 1
			sumRow.append(rowScore)
		return sumRow

    def CmdPickRow(self):
		row = self.infoGame["rows"]
		sumRow = self.Xscore(row)
        return sumRow
    def ProcessInfo(self):
        line = sys.stdin.readline()
        if line == '':
            logging.info('No Input')
            sys.exit(1)
        data = line.strip().split('|')
        logging.info("Get Info " + str(line))
        if data[0] == 'INFO':
            if data[1] == 'SETUP':
                self.InfoSetup(eval(data[2]))
            elif data[1] == 'NEWGAME':
                self.InfoNewGame(eval(data[2]))
            elif data[1] == 'GAME':
                self.InfoGame(eval(data[2]))
            elif data[1] == 'MOVE':
                self.InfoMove(eval(data[2]))
            elif data[1] == 'SCORE':
                self.InfoScore(eval(data[2]))
            elif data[1] == 'GAMEEND':
                self.InfoGameEnd(eval(data[2]))
                return False
        elif data[0] == 'CMD':
            if data[1] == 'PICKCARD':
                self.Send(self.CmdPickCard())
            elif data[1] == 'PICKROW':
                self.Send(self.CmdPickRow())
        return True
    def Send(self, data):
        logging.info('Send Info ' + str(data))
        print str(data)
        sys.stdout.flush()
    def Start(self):
        while True:
            if not self.ProcessInfo():
                break

if __name__ == '__main__':
    ai = AI()
 
ai.Start()
