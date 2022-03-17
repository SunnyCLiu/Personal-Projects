# made by: Sunny Liu
# last edited: March 16th, 2021
# this game was inspired by the classic board game 'Guess Who': https://en.wikipedia.org/wiki/Guess_Who%3F
# must import list of 'mystery' people from a txt file (I put 'World History' as an example when I was studying for the AP World History exam with my friends)

import random

def rule():
  print ("\nRules/How to Play:\n-Alternate turns asking one question. The youngest player goes first.\n-On your turn, ask a question that can be answered with a 'yes' or 'no'.\n  -For example: 'Does your Mystery Person have blue eyes?'\n-If the answer is 'yes', then you know that all the people with brown eyes can be eliminated.\n-If the answer is 'no', then all of the people with blue eyes can be eliminated.\n-IMPORTANT: To eliminate a person, just type in their number shown on the left side of the screen and press enter (eg. 15; 3).\n  -Also could type in multiple numbers separated by a space (eg. 3 8 16; 12 2 9)\n-Keep taking turns asking questions until someone thinks they can guess who is on the opponent's Mystery Person.\n-When you are ready to guess who is on the Mystery Person, make your guess on your turn instead of asking a question.\n  -You cannot ask a question and guess on the same turn.\n  -If you guess wrong, you lose the game!\n  -If you guess right, you win the game!\n\nAdditional rules:\n-For a greater challenge, players can't ask questions about physical appearances\n  -For example: 'Is your Mystery Person blonde?'\n-Instead, only questions about personality/characteristics are allowed\n  -For example: 'Does your Mystery Person have a good relationship with their parents?'\n\nYou can always review the rules during the game by entering 'rules'.\n")

  input("Press enter to continue")

selections = "\nCurrent selections: World History, Demon Slayer, Attack on Titan"

#introduction
print ("Welcome to Guess Who: Custom Edition!\nMade by Sunny Liu\n")

#rules/how to play
rules = input("Do you want to view the rules/how to play? (yes/no)\n(It is recommended for first time players, but you can always review the rules during the game by entering 'rules'): ").lower()

#user error
while not (rules == "yes" or rules == "no"):
  rules = input("Please enter either 'yes' or 'no': ").lower()
if rules == "yes":
  rule()

"""
#selections
print (selections)
selection = input("Choose a selection (capitalization doesn't matter): ").lower()

#opening files (also user error)
lines = []
while True:
  try:
    file = open(selection + ".txt")
    break
  except:
    if selection == "rules":
      rule()
      print (selections)
      selection = input("Choose a selection (spelling matters, capitalization doesn't): ").lower()
    else:
      selection = input("Invalid selection. Enter a selection: ").lower()
for line in file:
  lines.append(line.strip())
"""

lines = ['Kublai Khan', 'Marco Polo', 'Mansa Musa', 'Zheng He', 'Martin Luther', 'Suleiman I', 'Akbar the Great', 'Thomas Hobbes', 'John Locke', 'Rousseau', 'Adam Smith', 'Simon Bolivar', 'Matthew Perry', 'Karl Marx', 'Mahatma Gandhi', 'Vladimir Lenin', 'Joseph Stalin', 'Benito Mussolini', 'Adolf Hitler', 'Ho Chi Minh', 'Mao Zedong', 'Nelson Mandela']
#lines.sort()

#randomly gives mystery person
mystery = lines[random.randint(0, len(lines) - 1)]
print ("\nYour MYSTERY PERSON is: " + mystery)
input("\nPress enter to continue")

#main game: keeps going until one suspect left
while len(lines) > 1:

  #prints out mystery person and list of suspects
  print ("\nYour MYSTERY PERSON: " + mystery)
  for i in range(1, len(lines) + 1):
    print (str(i) + ": " + lines[i - 1])

  #asks player which nums to remove
  nums = input("\nWhich number(s) to remove?: ").lower()

  while True:
    try:

      #if only remove one number
      if not " " in nums:
        nums = int(nums)

        if nums <= 0:
          raise Exception
        #confirm answer
        confirm = input("Are you sure you want to remove " + lines[nums - 1] + "? (yes/no): ").lower()
        while not (confirm == "yes" or confirm == "no" or confirm == "rules"):
          confirm = input("Please enter either 'yes' or 'no': ").lower()
        if confirm == "no":
          break
        elif confirm == "rules":
          rule()
          break

        #delete entry
        del lines[nums - 1]

      #multiple numbers (separated by space)
      else:
        nums = nums.split(" ")
        #removes duplicates
        finalNums = []
        for i in nums:
          if int(i) <= 0:
            raise Exception
          if not i in finalNums:
            finalNums.append(i)

        #check if the amount to remove isn't the amount of the list, which will result in error
        if len(finalNums) == len(lines):
          raise Exception

        #confim answer
        confirmNums = []
        for i in finalNums:
          confirmNums.append(lines[int(i) - 1])
        confirmNums = ", ".join([str(i) for i in confirmNums])
        confirm = input("Are you sure you want to remove " + confirmNums + "? (yes/no): ").lower()
        while not (confirm == "yes" or confirm == "no" or confirm == "rules"):
          confirm = input("Please enter either 'yes' or 'no': ").lower()
        if confirm == "no":
          break
        elif confirm == "rules":
          rule()
          break

        #delete entries
        for i in range(len(finalNums)):
          finalNums[i] = int(finalNums[i])
        finalNums.sort()
        for i in range(len(finalNums)):
          del lines[finalNums[i] - i - 1]
      break

    #user error
    except:
      #instructions if help needed
      if nums == "help":
        print ("\nValid inputs include a single integer (eg. 15; 3) or integers separated by a space (eg. 3 8 16; 12 2 9)\nCommon inputing mistakes include:\n-Using any keywords other than integers and spaces (except for 'help' or 'rules')\n-Entering numbers out of range of numbers on the list\n-Entering an amount of numbers that is equal to or exeeds the amount on list\n")
        nums = input("Which number(s) to remove?: ").lower()
      elif nums == "rules":
        rule()
        break
      else:
        nums = input("Invalid input. Which number(s) to remove? (enter 'help' for help on inputing): ").lower()

#final mystery suspect
print ("\nFinal MYSTERY PERSON suspect: " + lines[0])
print ("\n\n")
