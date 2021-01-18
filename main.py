#import libraries and model
from replit import clear
from random import choice
from art import logo
from art import vs
from game_data import data


def game():
  #showing the game title
  print(logo)
  
  #function to pick data for comparising
  def pick_data():
    pick = choice(data)
    return pick
  
  #function to check the one with highest follower
  def check(entry_a, entry_b):
    if entry_a > entry_b:
      return "A"
    else:
      return "B"
  
  #function to printout select data
  def printout(select_a, select_b):
    print(f"Compare A: {select_a['name']}, a {select_a['description']} from {select_a['country']}")
    print(vs)
    print(f"Compare B: {select_b['name']}, a {select_b['description']} from {select_b['country']}")

  #initialization
  A = pick_data()
  data.remove(A)
  B = pick_data()
  data.append(A)
  printout(A,B)

  playing = True

  score = 0
  #game logic
  while playing:
    #take user input
    user =  input("Who has more follower? Type 'A' or 'B'  ").upper()

    #get number of follower of the selected data
    follower_a = A['follower_count']
    follower_b = B['follower_count']
    #compare
    result = check(follower_a, follower_b)

    #check if user choice is correct
    if result ==  user:
      score += 1
      A =  B
      data.remove(A)
      B = pick_data()
      data.append(A)
      clear()
      print(logo)
      print(f"You are right. Current score {score}")
      printout(A,B)

    else:
      clear()
      print(logo)
      print(f"Sorry that's wrong. Final Score {score}")
      playing = False

game()
