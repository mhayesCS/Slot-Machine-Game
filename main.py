import random 

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


ROWS = 3
COLS = 3


symbols = {
    "bear": 4, 
    "horse": 4, 
    "star": 6, 
    "moon": 6,
}

symbols_value = {
    "bear": 4, 
    "horse": 4, 
    "star": 6, 
    "moon": 6,
}

def check_earnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_2_check = column[line]
            if symbol != symbol_2_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines + 1)

    return winnings, winning_lines








def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []

    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    #defined columns list 

    for _ in range(cols):
        #generate columns for the amount of columns we have which is 3 so this for loop is ran 3 times 
        
        #column is an empty list 
        column = []
        #current symbols is equal to a copy all symbols
        current_symbols = all_symbols[:]

        # loop through the # of values we need to generate which is = to the # of rows which is also 3
        for _ in range(rows):
            # picks random value from current symbols list
            value = random.choice(current_symbols)
            # we remove it so we don't pick the same choice again
            current_symbols.remove(value)
            # add the value to our columns list 
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end= " | ")
            else: 
                print(column[row], end= "")
        print()



def deposit():
    while True:
        amount = input('Enter Deposit Amount: $ ')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0: 
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount 



def get_number_of_line():
    while True:
        lines = input("Enter The Number of Lines to bet on: (1-" + str(MAX_LINES) + ")? " )
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES: 
                break
            else:
                print("# of Lines must be less than or equal 3.")
        else:
            print("Please enter a number.")
    return lines


def get_bet():
    while True:
        amount = input('Enter bet amount for each line: $ ')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET : 
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("Please enter a number.")
    return amount 


def spin(balance):
    lines = get_number_of_line()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You have an insuffient balance to bet, you're current balance is ${balance}, your bet was ${bet}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total Bet = ${total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbols)
    print_slot_machine(slots)
    winnings, winning_lines = check_earnings(slots, lines, bet, symbols_value)
    print(f"You won ${winnings}")
    print(f"You won on lines: ", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        user = input("Press enter to play (q to quit) ")
        if user == 'q':
            break
        balance += spin(balance)
        
    print(f"You left with ${balance}")       




main()