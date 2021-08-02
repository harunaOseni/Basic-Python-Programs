# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# (<12 "$5") (12 - 8 "$7") (> 18 "$12")

# print("Welcome to the rollercoaster")

# height = int(input("What is your height in cm ?"))

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("How old are you ?"))
#     if age < 12:
#         print("Please pay $5")
#         bill = 5
#     elif age >= 12 and age < 18:
#         print("Please pay $7")
#         bill = 7
#     elif age >= 45 and age <= 55:
#         print("You're riding for free guys!!!")
#         bill = 0
#     else:
#         print("Please pay $12")
#         bill = 12

#     want_photos = input("Do you want photos? (Y/N)")
#     if want_photos == "Y" or want_photos == "y":
#         bill += 3
#         print("Your total is $" + str(bill))
#     else:
#         print("Your total is $" + str(bill))
# else:
#     print("Sorry, you have to grow taller before you \
# can ride the rollercoaster!")


# BMI calculator
# weight = int(input("Enter your weight in kg: "))
# height = float(input("Enter your height in cm: "))

# Bmi = round(weight / (height ** 2))

# if Bmi < 18.5:
#     print(f"Your BMI is {Bmi}, You are underweight")
# elif Bmi >= 18.5 and Bmi < 25:
#     print(f"Your BMI is {Bmi}, You are normal weight")
# elif Bmi >= 25 and Bmi < 30:
#     print(f"Your BMI is {Bmi}, You are slightly overweight")
# elif Bmi >= 30 and Bmi < 35:
#     print(f"Your BMI is {Bmi}, You are Obese")
# elif Bmi >= 35:
#     print(f"Your BMI is {Bmi}, You are clinically obese")

# leap year calculator

# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# Python Pizza Delivery program

# print("Welcome to Python Pizza Delivery")

# small_pizza = 15
# medium_pizza = 20
# large_pizza = 25
# pepperoni_for_small_pizza = 2
# pepperoni_for_medium_pizza_or_large_pizza = 3
# extra_cheese_for_pizza = 1


# pizza_size = input("What size pizza do you want? S, M or L: ")

# if pizza_size == "S" or pizza_size == "s":
#     pizza_size = small_pizza
#     want_pepperoni = input("Do you want pepperoni? (Y/N) ")
#     if want_pepperoni == "Y" or want_pepperoni == "y":
#         pizza_size += pepperoni_for_small_pizza
#     want_extra_cheese = input("Do you want extra cheese? (Y/N) ")
#     if want_extra_cheese == "Y" or want_extra_cheese == "y":
#         pizza_size += extra_cheese_for_pizza
#         print(f"Your total bill ${pizza_size}")

# elif pizza_size == "M" or pizza_size == "m":
#     pizza_size = medium_pizza
#     want_pepperoni = input("Do you want pepperoni? (Y/N) ")
#     if want_pepperoni == "Y" or want_pepperoni == "y":
#         pizza_size += pepperoni_for_medium_pizza_or_large_pizza
#     want_extra_cheese = input("Do you want extra cheese? (Y/N) ")
#     if want_extra_cheese == "Y" or want_extra_cheese == "y":
#         pizza_size += extra_cheese_for_pizza
#         print(f"Your total bill ${pizza_size}")

# elif pizza_size == "L" or pizza_size == "l":
#     pizza_size = large_pizza
#     want_pepperoni = input("Do you want pepperoni? (Y/N) ")
#     if want_pepperoni == "Y" or want_pepperoni == "y":
#         pizza_size += pepperoni_for_medium_pizza_or_large_pizza
#     want_extra_cheese = input("Do you want extra cheese? (Y/N) ")
#     if want_extra_cheese == "Y" or want_extra_cheese == "y":
#         pizza_size += extra_cheese_for_pizza
#         print(f"Your total bill ${pizza_size}")

# Love calculator program
# my_name = input("What is your name?\n")

# their_name = input("What is the name of the person you are attracted to?\n")

# both_names_concatenated = my_name + " " + their_name

# both_names_concatenated_lowercase = both_names_concatenated.lower()

# # true count
# true_count_t = both_names_concatenated_lowercase.count("t")
# true_count_r = both_names_concatenated_lowercase.count("r")
# true_count_u = both_names_concatenated_lowercase.count("u")
# true_count_e = both_names_concatenated_lowercase.count("e")

# total_true_count = true_count_t + true_count_r + true_count_u + true_count_e

# # love count
# love_count_l = both_names_concatenated_lowercase.count("l")
# love_count_o = both_names_concatenated_lowercase.count("o")
# love_count_v = both_names_concatenated_lowercase.count("v")
# love_count_e = both_names_concatenated_lowercase.count("e")

# total_love_count = love_count_l + love_count_o + love_count_v + love_count_e

# true_love_score = str(total_true_count) + str(total_love_count)

# true_love_score_int = int(true_love_score)

# if true_love_score_int <= 10 or true_love_score_int >= 90:
#     print(
#         f"Your score is {true_love_score_int},\
# you go togther like coke and mentos")

# elif true_love_score_int >= 40 and true_love_score_int <= 50:
#     print(f"Your score is {true_love_score_int}, you are alright together.")

# else:
#     print(f"Your score is {true_love_score_int}")

# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')

# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")

# name_of_player = input("Input your user name: ")

# first_chapter = input(f"It was a sunny day, when {name_of_player}\
#  was still in search of the golden treasure in the highland of norway\
#  and found himself stuck between two paths with a decision,  to choose \
#  either the 'left' or 'right' path, choose a path:\n")

# if first_chapter == "right":
#     print('''
#     you just entered the path contained with wild animals\
#  and you were eaten by a wild lion.\n 

#                                                 ,w.
#                                               ,YWMMw  ,M  ,
#                          _.---.._   __..---._.'MMMMMw,wMWmW,
#                     _.-""        """           YP"WMMMMMMMMMb,
#                  .-' __.'                   .'     MMMMW^WMMMM;
#      _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
#   ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\
#  ,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,
#  WMMm__,-'.'     /      _.\      F"""-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
#  "^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|
#             /   .'            ; ;         )  )`{  \ `"^W^`,   \  :
#            /  .'             /  (       .'  /     Ww._     `.  `"
#           /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
#  fsc     (--, )                `,_ / `) \/"")      ^"      `-, -;"\:
#           `"""                    `"""   `"'                  `---" 
#     ''')
# elif first_chapter == "left":
#     second_chapter = input("Congratulations, you just reached a checkpoint, blocking your\
#  path to getting the golden is an ocean, you can either choose to swim and get to the next destination\
#  or wait for the ferry, specify your choice by typing, 'swim' or 'wait': \n")
#     if second_chapter == "swim":
#         print('''
#         Oh snap, you should have waited, you were killed by an hungry octopus\n
#                    ___
#                      .-'   `'.
#                     /         \
#                     |         ;
#                     |         |           ___.--,
#            _.._     |0) ~ (0) |    _.---'`__.-( (_.
#     __.--'`_.. '.__.\    '--. \_.-' ,.--'`     `""`
#    ( ,.--'`   ',__ /./;   ;, '.__.'`    __
#    _`) )  .---.__.' / |   |\   \__..--""  """--.,_
#   `---' .'.''-._.-'`_./  /\ '.  \ _.-~~~````~~~-._`-.__.'
#         | |  .' _.-' |  |  \  \  '.               `~---`
#          \ \/ .'     \  \   '. '-._)
#           \/ /        \  \    `=.__`~-.
#      jgs  / /\         `) )    / / `"".`\
#     , _.-'.'\ \        / /    ( (     / /
#      `--~`   ) )    .-'.'      '.'.  | (
#             (/`    ( (`          ) )  '-;
#              `      '-;         (-'
#         ''')
#     elif second_chapter == "wait":
#         third_chapter = input("Finally, you have have arrived at the finale, standing at your path\
#  are three doors, a yellow, blue and a red door, behind one of these doors\
#  lies the golden treasure, which door will you be entering ?, choose 'yellow' \
#  'blue' or 'red': \n")
#         if third_chapter == "yellow":
#             print(" Congratulations, you have won the game, you have found the golden treasure,you have \
# completed your quest and you are the true hero.")
#             print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')

#         elif third_chapter == "blue":
#             print('''
#             Uh Oh! You have been eaten by a huge beast, Game Over.
#                 (    )
#                   ((((()))
#                   |o\ /o)|
#                   ( (  _')
#                    (._.  /\__
#                   ,\___,/ '  ')
#     '.,_,,       (  .- .   .    )
#      \   \\     ( '        )(    )
#       \   \\    \.  _.__ ____( .  |
#        \  /\\   .(   .'  /\  '.  )
#         \(  \\.-' ( /    \/    \)
#          '  ()) _'.-|/\/\/\/\/\|
#              '\\ .( |\/\/\/\/\/|
#                '((  \    /\    /
#                ((((  '.__\/__.')
#                 ((,) /   ((()   )
#                  "..-,  (()("   /
#             pils  _//.   ((() ."
#           _____ //,/" ___ ((( ', ___
#                            ((  )
#                             / /
#                           _/,/'
#                         /,/,"
#             ''')
#         elif third_chapter == "red":
#             print('''
#             UH OH! The room was filled with fire, you got burnt, Game Over.
            
#                (  .      )
#            )           (              )
#                  .  '   .   '  .  '  .
#         (    , )       (.   )  (   ',    )
#          .' ) ( . )    ,  ( ,     )   ( .
#       ). , ( .   (  ) ( , ')  .' (  ,    )
#      (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
#  jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#             ''')

#hangman program 
# from hangman_words import *
# from hangman_art import logo, stages
# import random

# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
# end_of_game = False
# lives = 6

# print(logo)

# display = []
# for _ in range(word_length):
#     display += "_"

# while not end_of_game:
#     guess = input("Guess a letter: ").lower()

#     if guess in display:
#         print(
#             f"You've already guessed the letter {guess}, try another letter!")

#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter
#     if guess not in chosen_word:
#         print(f"{guess} is not in the word, you lose a life!")
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")

#     print(f"{' '.join(display)}")

#     if "_" not in display:
#         end_of_game = True
#         print("You win.")
#     print(stages[lives])

