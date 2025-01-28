import utils as ut
import player as pl
import rooms

def initGame():
    username = input("Enter Your username : ")
    while (not ut.validateUsername(username)):
        print("Username Must have 4 digits at least!!!")
        username = input("Enter Your username : ")

    password = input("Enter Your Password : ")
    while (not ut.validatePassword(password)):
        print("Password Must have 7 digits at least!!!")
        password = input("Enter Your Password : ")

    player = pl.Player(username, password)
    
    while (not player.finishGame()):
        player.addPoint(rooms.getUserScore())
        player.addPlay()
        print(player.showProfile())
