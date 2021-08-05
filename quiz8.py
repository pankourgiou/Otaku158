import random

class QA:
  def __init__(self, question, correctAnswer, otherAnswers):
    self.question = question
    self.corrAnsw = correctAnswer
    self.otherAnsw = otherAnswers

qaList = [QA("Which is Iron Maiden's second album?", "Killers", ["Iron Maiden", "Piece of Mind"]),
QA("Which is Iron Maiden's fourth album?", "Piece of Mind", ["Iron Maiden", "Brave New World", "Fear of the dark"]),
QA("Which is Iron Maiden's third album?", "The Number of the beast", ["Book of Souls", "Fear of the dark", "Killers"]),
QA("Which is the first song from Iron Maiden's Piece of mind album?", "Where Eagles dare", ["The Trooper", "Fear of the dark"]),
QA("Which is the fifth song from Iron Maiden's Piece of mind album?", "The Trooper", ["Fear of the dark", "Phantom of the opera", "Flight of the Icarus", "Die with your boots on"])]

corrCount = 0
random.shuffle(qaList)
for qaItem in qaList:
  print(qaItem.question)
  print("Possible answers are:")
  possible = qaItem.otherAnsw + [qaItem.corrAnsw] # square brackets turn correct answer into list for concatenating with other list
  random.shuffle(possible)
  count = 0 # list indexes start at 0 in python
  while count < len(possible):
    print(str(count+1) + ": " + possible[count])
    count += 1
  print("Please enter the number of your answer:")
  userAnsw = input()
  while not userAnsw.isdigit():
    print("That was not a number. Please enter the number of your answer:")
    userAnsw = input()
  userAnsw = int(userAnsw)
  while not (userAnsw > 0 and userAnsw <= len(possible)):
    print("That number doesn't correspond to any answer. Please enter the number of your answer:")
    userAnsw = input()
  if possible[userAnsw-1] == qaItem.corrAnsw:
    print("Your answer was correct.")
    corrCount += 1
  else:
    print("Your answer was wrong.")
    print("Correct answer was: " + qaItem.corrAnsw)
  print("")

print("You answered " + str(corrCount) + " of " + str(len(qaList)) + " questions correctly.")
