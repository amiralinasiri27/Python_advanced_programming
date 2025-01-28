class Player:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.points = 0
        self.totalPlays = 0

    def addPoint(self, score):
        self.points += score

    def addPlay(self):
        self.totalPlays += 1

    def showProfile(self):
        print(f"---------------------------- {self.username} ----------------------------")
        print("Games Played :", self.totalPlays)
        print("Total Score :", self.points)

    def finishGame(self):
        finishState = input("Do You Want To Play another Game? Y/N : ")
        if finishState == 'N':
            return True
        return False