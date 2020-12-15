class Board(object):
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.board = list(range(60))
        self.slideSquares = [5, 20, 35, 50]
        self.homeSlides = [12, 27, 42, 57]

    def slideAllPieces(self):
        for i in range(1, 5):
            # regular slides
            if self.p1.getPawnLocation(i) in self.slideSquares:
                self.p1.pawns[i] += 4
            if self.p2.getPawnLocation(i) in self.slideSquares:
                self.p2.pawns[i] += 4
            if self.p3.getPawnLocation(i) in self.slideSquares:
                self.p3.pawns[i] += 4
            if self.p4.getPawnLocation(i) in self.slideSquares:
                self.p4.pawns[i] += 4
            if self.p1.getPawnLocation(i) in self.homeSlides:
                self.p1.pawns[i] += 3
            if self.p2.getPawnLocation(i) in self.homeSlides:
                self.p2.pawns[i] += 3
            if self.p3.getPawnLocation(i) in self.homeSlides:
                self.p3.pawns[i] += 3
            if self.p4.getPawnLocation(i) in self.homeSlides:
                self.p4.pawns[i] += 3
