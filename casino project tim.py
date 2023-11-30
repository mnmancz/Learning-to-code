# we need to get the deposit the user is entering, as well as their bet
import random

# if you do /n, this tells the data to go to the next line

MAX_LINES = 3       # This is known as a global constant
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,    # symbol is going to be A, symbol_count is going to be 2
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]  # saying to check the symbol at whatever column we are at
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines + 1)           # have to do plus one because its an index

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):    #easiest way is to make a list of all of th evalues we could select from
    all_symbols = []
    for symbol, symbol_count in symbols.items():          # symbol is the key, symbol_count is the value
        for _ in range(symbol_count):
            all_symbols.append(symbol)              # remember that [] are equal to a list

    columns = []                            # we are defining our columns list
    for _ in range(cols):                 # we are generating a column for every single column that we have
        column = []                         # we are saying that a column is equal to an empty list
        current_symbols = all_symbols[:]    # the colon means that it is a copy, we are saying that the current symbols that we can select from is equal to a copuy of all symbols
        for _ in range(rows):               # loop through the number of values we need to generate, which is equal to the number of rows in the slot machine
            value = random.choice(current_symbols) # if there is two A's, we need to make sure that one of the A's have been removed. It is choosing a random value from the symbols that we have
            current_symbols.remove(value)    # this is so we don't pick that value again
            column.append(value)             # we are adding that value to our column

        columns.append(column)     # we are going to append the current column, and add it to our columns list

    return columns


def print_slot_machine(columns):       # we need to flip around our rows and columns
    for row in range(len(columns[0])):                # number of rows is how many elements are in each column, if we passd something that had no columns, this would crash. len(columns[0]): This part calculates the length of the first element (columns[0]) in the columns list. Assuming columns is a list of lists or a 2D array, columns[0] refers to the first row of the 2D structure, and len(columns[0]) gives the number of elements (columns) in that row.
        for i, column in enumerate(columns):         # looping through values in each column, when you enumerate it gives you the index
            if i != len(columns) - 1:       # checking if i is not equal to the length of columns - 1, it is the maximum element to access in the columns list
                print(column[row], end=" | ")    # this is a pipe operator, only want to pipes in the middle, not at the very end
            else:
                print(column[row], end="")        # over all this transposes our columns and flips them, we want this empty string at the end so it moves to the next row


        print()

        
def deposit():        #need the user to keep entering an amount until its one that's valid
    while True:
        amount = input("What would you like to deposit? $")       # this will come as a string
        if amount.isdigit():             # the .isdigit lets us know if it's a valid whole number, they won't be able to enter a negative number or decimals
            amount = int(amount)           # we want to convert it from a string to a integer
            if amount > 0:               # deposit cannot be negative
                break
            else:
                print("Invalid amount, please try again. Amount must be > 0")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ").")       # converts the string to an input
        if lines.isdigit():             # the .isdigit lets us know if it's a valid whole number, they won't be able to enter a negative number or decimals
            lines = int(lines)           # we want to convert it from a string to a integer
            if 1 <= lines <= MAX_LINES:               # we are checking to see if a value is in between two values, could be useful for battery testing voltages
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet $")       
        if amount.isdigit():             # the .isdigit lets us know if it's a valid whole number, they won't be able to enter a negative number or decimals
            amount = int(amount)           # we want to convert it from a string to a integer
            if MIN_BET <= amount <= MAX_BET:               # we are checking to see if a value is in between two values, could be useful for battery testing voltages
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")     # as long as it's in the curly brakets, it is converted to a string
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough money to bet this much, your current balance is ${balance}")
        else: 
            break
    

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet} ")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
   
    print(f"You left with ${balance}")

main()
