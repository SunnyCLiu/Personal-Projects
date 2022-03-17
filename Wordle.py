# made by: Sunny Liu
# last edited: March 10th, 2022
# this game is a spin-off of Wordle, a popular web-based game: https://www.nytimes.com/games/wordle/index.html

import random

# reads input.txt file and put all words in a list
"""inputs = []
file = open("words.txt", "r")
for line in file:
  inputs.append(line.strip().lower())"""
inputs = ['abuse', 'adult', 'agent', 'anger', 'apple', 'aroma', 'award', 'basic', 'basis', 'beach', 'birth', 'block', 'blood', 'board', 'brain', 'bread', 'break', 'brown', 'buyer', 'cause', 'chain', 'chair', 'chest', 'chief', 'child', 'china', 'claim', 'class', 'clock', 'coach', 'coast', 'court', 'cover', 'cream', 'crime', 'cross', 'crowd', 'crown', 'cycle', 'dance', 'death', 'depth', 'doubt', 'draft', 'drama', 'dream', 'dress', 'drink', 'drive', 'earth', 'enemy', 'entry', 'error', 'event', 'fairy', 'faith', 'fault', 'field', 'fight', 'final', 'floor', 'focus', 'force', 'frame', 'frank', 'front', 'fruit', 'glass', 'grant', 'grass', 'green', 'group', 'guide', 'heart', 'horse', 'hotel', 'house', 'image', 'index', 'input', 'issue', 'judge', 'knife', 'layer', 'level', 'light', 'limit', 'lunch', 'major', 'march', 'match', 'metal', 'model', 'money', 'month', 'motor', 'mouth', 'music', 'night', 'noise', 'north', 'novel', 'nurse', 'offer', 'order', 'other', 'owner', 'panel', 'paper', 'party', 'peace', 'phase', 'phone', 'piece', 'pilot', 'pitch', 'place', 'plane', 'plant', 'plate', 'point', 'pound', 'power', 'press', 'price', 'pride', 'prize', 'proof', 'queen', 'radio', 'range', 'ratio', 'reply', 'right', 'river', 'rhino', 'round', 'route', 'rugby', 'scale', 'scene', 'scope', 'score', 'sense', 'shape', 'share', 'sheep', 'sheet', 'shift', 'shirt', 'shock', 'sight', 'skill', 'sleep', 'smile', 'smoke', 'sound', 'south', 'space', 'speed', 'spite', 'sport', 'squad', 'staff', 'stage', 'start', 'state', 'steam', 'steel', 'stock', 'stone', 'store', 'storm', 'study', 'stuff', 'style', 'sugar', 'table', 'taste', 'theme', 'thing', 'title', 'total', 'touch', 'tower', 'track', 'trade', 'train', 'trend', 'trial', 'trust', 'truth', 'uncle', 'union', 'unity', 'value', 'video', 'visit', 'voice', 'waste', 'watch', 'water', 'while', 'white', 'whole', 'woman', 'world', 'youth']
# class with all the colors used in wordle
class color:
  green = '\033[32m'
  yellow = '\033[33m'
  end = '\033[0m'

# function that takes in a word and makes sure that it's valid (length of 5)
def enterWord():
  word = ""
  while (len(word) != 5):
    word = input("Please enter a word (5 letters long): ").lower()
    if (len(word) > 5):
      print ("Word too long")
    elif (len(word) < 5):
      print ("Word too short")
  return (word)

# function that prints the 5x6 diagram
def printDiagram():
  for line in lines:
    row = ""
    for char in line:
      row = row + char + " "
    print (row)

# introduction
print ("Welcome to Wordle!! By Sunny Liu")

# loops forever in case user wants to play forever...
while True:
  # picking random index
  rand = random.randint(0, len(inputs) - 1)
  # setting random answer based on random index
  answer = list(inputs[rand])
  # creating original diagram
  lines = [["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"]]
  printDiagram()

  # loops through code 6 times because there's 6 guesses/lines
  for guess in range(0, 6):
    lines[guess] = [] # setting list to lines so it's easier to append the user's guess
    word = enterWord()
    for char in word:
      lines[guess].append(char)
    temp = answer.copy() # must copy the list because if I didn't they would reference the same list
    count = 0

    # marking GREEN algorithm
    for char in range(len(lines[guess])):
      # if the character in the guess and answer match...
      if lines[guess][char] == answer[char]: # (2D lists!!!)
        lines[guess][char] = color.green + lines[guess][char] + color.end # makes character green
        temp[char] = "" # must change the value to something else so the algorithm for checking the yellows doesn't get confused (that's why I need the temporary list). i could also remove it, but it's too much of a hassle since the indexes would be off
        count += 1

    # if they get all 5 characters green/correct, it breaks out of the loop
    if (count == 5):
      printDiagram()
      break

    # marking yellow algorithm
    for char in range(len(lines[guess])):
      if lines[guess][char] != answer[char]: # making sure I don't accidentally mark a green one yellow
        if lines[guess][char] in temp:
          temp.remove(lines[guess][char]) # removing it so it can't be used again (easier than changing it to "")
          lines[guess][char] = color.yellow + lines[guess][char] + color.end # making color yellow
    printDiagram()

  # conclusion
  # if they get all 5 characters in the word green
  if (count == 5):
    print ("Congratulations! The word was '" + "".join([str(elem) for elem in answer])
  + "'")
  # else (if they used up their 5 turns)
  else:
    print ("Sorry, you're out of guesses. The word was '" + "".join([str(elem) for elem in answer]) + "'")

  # play again option
  answer = input("Play again? (yes/no) ").lower()
  while not(answer == "yes" or answer == "no"):
    answer = input("Please enter a valid yes/no ").lower()
  
  # if user doesn't want to play again, break out of forever loop
  if (answer == "no"):
    break


"""
to do list:
spellchecker
make sure input is valid (no spaces, numbers, etc) => but most should be covered by the spellchecker
beta test & debugging
"""
