class Player(object):

    def __init__(self):
        self.pawns = {1 : "Start"
                      2 : "Start"
                      3 : "Start"
                      4 : "Start"}
    
    def getPawnLocation(self, pawnNum):
        return self.pawns[pawnNum]
    
    def whoToApplyCardTo(self, card):
        return 1
    
    def movePawn(self, pawnNum, newLocation):
        self.pawns[pawnNum] = newLocation

    def printPlayerInfo(self):
        print(self.pawns)
