Rollercoaster ride program
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

(<12 "$5") (12 - 8 "$7") (> 18 "$12")

print("Welcome to the rollercoaster")

height = int(input("What is your height in cm ?"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you ?"))
    if age < 12:
        print("Please pay $5")
        bill = 5
    elif age >= 12 and age < 18:
        print("Please pay $7")
        bill = 7
    elif age >= 45 and age <= 55:
        print("You're riding for free guys!!!")
        bill = 0
    else:
        print("Please pay $12")
        bill = 12

    want_photos = input("Do you want photos? (Y/N)")
    if want_photos == "Y" or want_photos == "y":
        bill += 3
        print("Your total is $" + str(bill))
    else:
        print("Your total is $" + str(bill))
else:
    print("Sorry, you have to grow taller before you \
can ride the rollercoaster!")


BMI calculator program
weight = int(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

Bmi = round(weight / (height ** 2))

if Bmi < 18.5:
    print(f"Your BMI is {Bmi}, You are underweight")
elif Bmi >= 18.5 and Bmi < 25:
    print(f"Your BMI is {Bmi}, You are normal weight")
elif Bmi >= 25 and Bmi < 30:
    print(f"Your BMI is {Bmi}, You are slightly overweight")
elif Bmi >= 30 and Bmi < 35:
    print(f"Your BMI is {Bmi}, You are Obese")
elif Bmi >= 35:
    print(f"Your BMI is {Bmi}, You are clinically obese")

leap year calculator

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

Python Pizza Delivery program

print("Welcome to Python Pizza Delivery")

small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_for_small_pizza = 2
pepperoni_for_medium_pizza_or_large_pizza = 3
extra_cheese_for_pizza = 1


pizza_size = input("What size pizza do you want? S, M or L: ")

if pizza_size == "S" or pizza_size == "s":
    pizza_size = small_pizza
    want_pepperoni = input("Do you want pepperoni? (Y/N) ")
    if want_pepperoni == "Y" or want_pepperoni == "y":
        pizza_size += pepperoni_for_small_pizza
    want_extra_cheese = input("Do you want extra cheese? (Y/N) ")
    if want_extra_cheese == "Y" or want_extra_cheese == "y":
        pizza_size += extra_cheese_for_pizza
        print(f"Your total bill ${pizza_size}")

elif pizza_size == "M" or pizza_size == "m":
    pizza_size = medium_pizza
    want_pepperoni = input("Do you want pepperoni? (Y/N) ")
    if want_pepperoni == "Y" or want_pepperoni == "y":
        pizza_size += pepperoni_for_medium_pizza_or_large_pizza
    want_extra_cheese = input("Do you want extra cheese? (Y/N) ")
    if want_extra_cheese == "Y" or want_extra_cheese == "y":
        pizza_size += extra_cheese_for_pizza
        print(f"Your total bill ${pizza_size}")

elif pizza_size == "L" or pizza_size == "l":
    pizza_size = large_pizza
    want_pepperoni = input("Do you want pepperoni? (Y/N) ")
    if want_pepperoni == "Y" or want_pepperoni == "y":
        pizza_size += pepperoni_for_medium_pizza_or_large_pizza
    want_extra_cheese = input("Do you want extra cheese? (Y/N) ")
    if want_extra_cheese == "Y" or want_extra_cheese == "y":
        pizza_size += extra_cheese_for_pizza
        print(f"Your total bill ${pizza_size}")

Love calculator program
my_name = input("What is your name?\n")

their_name = input("What is the name of the person you are attracted to?\n")

both_names_concatenated = my_name + " " + their_name

both_names_concatenated_lowercase = both_names_concatenated.lower()

# true count
true_count_t = both_names_concatenated_lowercase.count("t")
true_count_r = both_names_concatenated_lowercase.count("r")
true_count_u = both_names_concatenated_lowercase.count("u")
true_count_e = both_names_concatenated_lowercase.count("e")

total_true_count = true_count_t + true_count_r + true_count_u + true_count_e

# love count
love_count_l = both_names_concatenated_lowercase.count("l")
love_count_o = both_names_concatenated_lowercase.count("o")
love_count_v = both_names_concatenated_lowercase.count("v")
love_count_e = both_names_concatenated_lowercase.count("e")

total_love_count = love_count_l + love_count_o + love_count_v + love_count_e

true_love_score = str(total_true_count) + str(total_love_count)

true_love_score_int = int(true_love_score)

if true_love_score_int <= 10 or true_love_score_int >= 90:
    print(
        f"Your score is {true_love_score_int},\
you go togther like coke and mentos")

elif true_love_score_int >= 40 and true_love_score_int <= 50:
    print(f"Your score is {true_love_score_int}, you are alright together.")

else:
    print(f"Your score is {true_love_score_int}")

Treasure Island Program

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

name_of_player = input("Input your user name: ")

first_chapter = input(f"It was a sunny day, when {name_of_player}\
 was still in search of the golden treasure in the highland of norway\
 and found himself stuck between two paths with a decision,  to choose \
 either the 'left' or 'right' path, choose a path:\n")

if first_chapter == "right":
    print('''
    you just entered the path contained with wild animals\
 and you were eaten by a wild lion.\n 

                                                ,w.
                                              ,YWMMw  ,M  ,
                         _.---.._   __..---._.'MMMMMw,wMWmW,
                    _.-""        """           YP"WMMMMMMMMMb,
                 .-' __.'                   .'     MMMMW^WMMMM;
     _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
  ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\
 ,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,
 WMMm__,-'.'     /      _.\      F"""-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
 "^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|
            /   .'            ; ;         )  )`{  \ `"^W^`,   \  :
           /  .'             /  (       .'  /     Ww._     `.  `"
          /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
 fsc     (--, )                `,_ / `) \/"")      ^"      `-, -;"\:
          `"""                    `"""   `"'                  `---" 
    ''')
elif first_chapter == "left":
    second_chapter = input("Congratulations, you just reached a checkpoint, blocking your\
 path to getting the golden is an ocean, you can either choose to swim and get to the next destination\
 or wait for the ferry, specify your choice by typing, 'swim' or 'wait': \n")
    if second_chapter == "swim":
        print('''
        Oh snap, you should have waited, you were killed by an hungry octopus\n
                   ___
                     .-'   `'.
                    /         \
                    |         ;
                    |         |           ___.--,
           _.._     |0) ~ (0) |    _.---'`__.-( (_.
    __.--'`_.. '.__.\    '--. \_.-' ,.--'`     `""`
   ( ,.--'`   ',__ /./;   ;, '.__.'`    __
   _`) )  .---.__.' / |   |\   \__..--""  """--.,_
  `---' .'.''-._.-'`_./  /\ '.  \ _.-~~~````~~~-._`-.__.'
        | |  .' _.-' |  |  \  \  '.               `~---`
         \ \/ .'     \  \   '. '-._)
          \/ /        \  \    `=.__`~-.
     jgs  / /\         `) )    / / `"".`\
    , _.-'.'\ \        / /    ( (     / /
     `--~`   ) )    .-'.'      '.'.  | (
            (/`    ( (`          ) )  '-;
             `      '-;         (-'
        ''')
    elif second_chapter == "wait":
        third_chapter = input("Finally, you have have arrived at the finale, standing at your path\
 are three doors, a yellow, blue and a red door, behind one of these doors\
 lies the golden treasure, which door will you be entering ?, choose 'yellow' \
 'blue' or 'red': \n")
        if third_chapter == "yellow":
            print(" Congratulations, you have won the game, you have found the golden treasure,you have \
completed your quest and you are the true hero.")
            print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

        elif third_chapter == "blue":
            print('''
            Uh Oh! You have been eaten by a huge beast, Game Over.
                (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
            ''')
        elif third_chapter == "red":
            print('''
            UH OH! The room was filled with fire, you got burnt, Game Over.
            
               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            ''')

hangman program 
from hangman_words import *
from hangman_art import logo, stages
import random

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(
            f"You've already guessed the letter {guess}, try another letter!")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"{guess} is not in the word, you lose a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])

ceaser cipher program 
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ended = False


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char not in alphabet:
            end_text += char 
        else: 
            position = alphabet.index(char) 
            new_position = position + shift_amount 
            end_text += alphabet[new_position] 
    print(f"Here's the {cipher_direction}d result: {end_text}")

print(logo)
ended = False

while not ended:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    want_to_go_again = input("Do you want to go again? Type 'yes' or 'no':\n")
    if want_to_go_again == "no":
        ended = True

if shift > 26:
    shift = shift % 26

Dictionaries, nesting...

student score program

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student in student_scores:
    if student_scores[student] <= 70:
        student_grades[student] = "Fail"
    elif student_scores[student] >= 71 and student_scores[student] <= 80:
        student_grades[student] = "Acceptable"
    elif student_scores[student] >= 81 and student_scores[student] <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] >= 91 and student_scores[student] <= 100:
        student_grades[student] = "Outstanding"

print(student_grades)

travel log program

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_country(country_name,  amount_of_visits, states_visited):
    travel_log.append(
        {
            "country": country_name,
            "visits": amount_of_visits,
            "cities": states_visited
        }
    )

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
starting_dictionary = {
    "a": 9,
    "b": 8,
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

auction bid program
import os

ended = False
auction_bid = {}

print("Welcome to the secret auction program.")


def highest_auction_bidder(auction_bid):
    highest_bid = 0
    highest_bidder = ""
    for bidder in auction_bid:
        if auction_bid[bidder] > highest_bid:
            highest_bid = auction_bid[bidder]
            highest_bidder = bidder
    print(
        f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}")


while not ended:
    bidder = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    auction_bid[bidder] = bid_amount
    next_bidder = input("Does anyone else want to bid?: Yes or no \n")
    if next_bidder == "no":
        # check for highest bidder
        os.system("clear||cls")
        highest_auction_bidder(auction_bid)
        ended = True
    elif next_bidder == "yes":
        os.system("clear||cls")
        ended = False

function with output
def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return f_name + " " + l_name

print(format_name("john", "smith"))


Leap year month program 
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        if month == 2:
            return f"The year is {year} is a leap year and the month {month} has {month_days[month - 1] + 1} days"
        else:
            return f"The year is {year} is a leap year and the month {month} has {month_days[month - 1]} days"
    else:
        return f"The year is {year} is not a leap year and the month {month} has {month_days[month - 1]} days"

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

calculator program
dictionary containing math operations

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

def power(n1, n2):
    return n1 ** n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power
}


def calculator():
    ended = False
    next_phase = False
    while not ended:
        num1 = float(input("What's the first number?: "))
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: ")) 
        calculation_function = operations[operation_symbol]
        first_answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {first_answer}")

        continue_calculation = input(
            f"Type 'y' to continue calculating with {first_answer} or type 'n' to restart: ")
        if continue_calculation == "n":
            calculator()
        else:
            while not next_phase:
                for symbol in operations:
                    print(symbol)
                operation_symbol = input("Pick an operation: ")
                num3 = float(input("What's the next number?: "))
                calculation_function = operations[operation_symbol]
                second_answer = calculation_function(first_answer, num3)

                print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

                continue_calculation = input(
                    f"Type 'y' to continue calculating with {second_answer} or type 'n' to restart calculator: ")
                if continue_calculation == "n":
                    next_phase = True
                    calculator()
                else:
                    next_phase = False
                    first_answer = second_answer


calculator()

#black jack terminal game program 

############### Blackjack Terminal Game #####################

#import random
import random
import os


def deal_to_players_hand():
    """function to deal random cards to both players hand"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score_of_hand(hand):
    """function used to calculate scores of each players hand"""
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)


def compare_player_and_dealers_hand(players_score, dealers_score, bet_amount):
    if players_score > 21 and dealers_score > 21:
        return f"You went over, You lost your ${bet_amount} bet!😪"
    elif players_score == 0:
        return f"You win, what a game😍! You won ${bet_amount + 100} bet!"
    elif dealers_score == 0:
        return f"Dealer has black jack, You lost your ${bet_amount} bet!😢"
    elif players_score == dealers_score:
        return f"You tied, what a game😍, you ${bet_amount} bet remains untouched!"
    elif players_score > 21:
        return f"You went over, You lost your ${bet_amount} bet, sad!😪"
    elif dealers_score > 21:
        return "Dealer went over, You win ${bet_amount + 100} bet!!😍!"
    elif players_score > dealers_score:
        return f"You win, what a game, You win the ${bet_amount + 100} bet!😍!"
    else:
        return f"Dealer wins, Better luck next time😢You lost your ${bet_amount} bet!"


def play_black_jack():
    print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")

    players_hand = []
    dealers_hand = []
    black_jack_is_running = True
    betting_amount = int(input("How much do you want to bet?: $")) 

    for i in range(2):
        players_hand.append(deal_to_players_hand())
        dealers_hand.append(deal_to_players_hand())

    while black_jack_is_running:
        players_score = calculate_score_of_hand(players_hand)
        dealers_score = calculate_score_of_hand(dealers_hand)
        print(f"Your hand: {players_hand}, current score: {players_score}")
        print(
            f"Dealers hand: {dealers_hand[0]}, current score: {dealers_score}")

        if players_score == 0 or dealers_score == 0 or players_score > 21 or dealers_score > 21:
            black_jack_is_running = False
        else:
            answer = input("Would you like to hit or stand? ")
            if answer == "hit":
                players_hand.append(deal_to_players_hand())
            else:
                black_jack_is_running = False
    while dealers_score < 17:
        dealers_hand.append(deal_to_players_hand())
        dealers_score = calculate_score_of_hand(dealers_hand)

    print(f"Your Final hand: {players_hand}, current score: {players_score}")
    print(
        f"Dealers Final hand: {dealers_hand}, current score: {dealers_score}")
    print(compare_player_and_dealers_hand(players_score, dealers_score, betting_amount))


your_name = input("Enter user name for black jack game? ")
while input("Would you like to play Black Jack? yes or no: ").lower() == "yes":
    os.system("clear||cls")
    play_black_jack()
else:
    print(f"Goodbye, {your_name}, be sure to come again!")
    

import random
logo = """
  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       
"""

# Number guessing game program


def random_number():
    return random.randint(1, 100)


def guess_number_comparison(guess, random_number, easy_attempt, hard_attempt):
    if guess == random_number:
        return f"Congratulations! You guessed the number {random_number} correctly😍😍!"
    if (guess != random_number and easy_attempt == 0) or (guess != random_number and hard_attempt == 0):
            return f"You ran out of attempts, the number was {random_number}, 😪😢."
    elif (guess < random_number and easy_attempt != 0) or (guess < random_number and hard_attempt != 0):
        return f"Your guess of {guess} was too low, try again mate."
    elif (guess > random_number and easy_attempt != 0) or (guess > random_number and hard_attempt != 0):
        return f"Your guess of {guess} was too high, try again mate."


def play_number_guessing_game():
    #print intro and logo 
    print(logo)
    print("Welcome to the number guessing game!😍")

    # set the initial values
    number = random_number()
    guess = 0
    easy_attempt = 10
    hard_attempt = 5
    choose_difficulty = input("Choose a difficulty (easy or hard): ")
    # loop until the guess is correct
    if choose_difficulty == "easy":
        while easy_attempt != 0 and guess != number:
            print(
                f"You have {easy_attempt} attempts remaining to guess the number.")
            guess = int(input("Make a guess "))
            easy_attempt -= 1
            print(guess_number_comparison(
                guess, number, easy_attempt, hard_attempt))
    elif choose_difficulty == "hard":
        while hard_attempt != 0 and guess != number:
            print(
                f"You have {hard_attempt} attempts remaining to guess the number.")
            guess = int(input("Make a guess "))
            hard_attempt -= 1
            print(guess_number_comparison(
                guess, number, easy_attempt, hard_attempt))


play_number_guessing_game()




# Higher Lower Game program
# import art.py and print game logo
from art import *
import random
from game_data import *
import os

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""
vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
""" 
print(logo)


# function to format sentence data to look the the example below
# e.g Katy Perry, a Musician, from United States.
def celebrity_summary(celebrity):
    celebrity_name = celebrity["name"]
    celebrity_description = celebrity["description"]
    celebrity_country = celebrity["country"]
    return f"{celebrity_name}, a {celebrity_description}, from {celebrity_country}"

# function to return answers in relation to following comparison
def followers_count_answer(guess, celebrityA_followers, celebrityB_followers):
    if celebrityA_followers > celebrityB_followers:
        return guess == "A"
    else:
        return guess == "B"


# main function to play the higher lower game
def play_higher_lower_game(celebrities_data):
    game_playing = True
    score = 0
    celebrity_B = random.choice(celebrities_data)

    while game_playing:
        celebrity_A = celebrity_B
        celebrity_B = random.choice(celebrities_data)

        if score >= 1:
            print(f"You're right! Current score: {score}")

        print(f"Celebrity A: {celebrity_summary(celebrity_A)}")
        print("")
        print(vs)
        print("")
        print(f"Celebrity B: {celebrity_summary(celebrity_B)}")

        guess = input(
            "Which of these two celebrities is more popular? A or B: ")
        is_guess_correct = followers_count_answer(
            guess, celebrity_A["follower_count"], celebrity_B["follower_count"])
        os.system("clear||cls")
        if is_guess_correct: 
            score += 1

        else:
            os.system("clear||cls")
            game_playing = False
            print(f"Sorry , that's wrong. Final score: {score}")


play_higher_lower_game(data) 
