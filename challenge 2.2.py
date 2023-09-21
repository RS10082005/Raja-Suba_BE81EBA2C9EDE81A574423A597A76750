"""Imlement a class called player that represents a cricket player. The player class should have a 
method called play() which prints "The player is playing cricket. Derive two classes,Batsman and
Bowler, from th player class. Override the play() method in each derived class to print "The batsman 
is batting" and "The bowler is bowling",respectively. Write a program to create objects of both the
Batsman and Bowler classes and call the play() method for each object"""


#define the base class Player
class Player:
  def Play(self):
    print("The player is playing cricket.")


#define the derived class Batsman
class Batsman(Player):
  def play(self):
    print("The batsman is batting")

#Define the derived class Bowler
class Bowler(Player):
  def play(self):
    print("The bowler is bowling")

#create objects of batsman and bowler classes
batsman = Batsman()
bowler = Bowler()

#call the play() method for each object
batsman.play()
bowler.play()