"""
projekt_2-Tic-Tac-Toe.py: druhý projekt do Engeto Online Python Akademie
author: David Herman
email: david.herman@seznam.cz
discord: DavidHerman#5014
"""
import os
separator = "=" * 40
score_p1 = 0
score_p2 = 0

# Uvítání a pravidla
print(f"""
Welcome to Tic Tac Toe
{separator}
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
Let's start the game!""")

print(separator)

# Definování hracího pole a ukázání čísel jednotlivých buněk
borders = "+---+---+---+"

print(f"""
{borders}
| 1 | 2 | 3 |
{borders}
| 4 | 5 | 6 |
{borders}
| 7 | 8 | 9 |
{borders}      
""")

print(separator)

player_1 = input("Enter name of the first player: ")
player_2 = input("Enter name of the second player: ")
j = 1 # Počítadlo her, zajišťuje střídání prvního hrážče během následujících her

while True: # Umožňuje hrát hru opakovaně

    #vynulování počítadel před další hrou
    i = 1 # Počítání kol, zajišťuje střídání hráčů během jedné hry 
    cells = ["", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ","   "] # Je jich 10 aby indexy odpovídaly zadaným číslům
    full_cells = [] # Seznam obsazených buněk
    cells_O = set() # Seznam buněk obsazených "O"
    cells_X = set() #Seznam buněk obsazených "X"
    victory = False


    while i <10: # 9 je maximální počet volných polí
        
        if (i % 2 == 1 and j % 2 == 1) or (i % 2 == 0 and j % 2 == 0): # Když je liché kolo v licé hře nebo sudé kolo v sudé hře - hraje hráč O
            while not (x := input(f"{player_1} | Please enter your move number: ")).isnumeric() or x in full_cells or int(x) not in range(1, 10): # ověření že vstup je validní
                print("Remember you must enter number of free cell!")

            cells[int(x)] = " O " # Nahrazení prázdné buňky znakem "O"
            cells_O.add(int(x)) # Množina buněk obsazených O

        elif (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0): # Když je sudé kolo v liché hře nebo liché kolo v sudé hře - hraje hráč X
            while not (x := input(f"{player_2}| Please enter your move number: ")).isnumeric() or x in full_cells or int(x) not in range(1, 10): # ověření že vstup je validní
                print("Remember you must enter number of free cell!")
            cells[int(x)] = " X " # Nahrazení prázdné buňky znakem "X"
            cells_X.add(int(x)) # Množina buněk obsazených X
    
        full_cells.append(x) # Přidání hodnoty do seznamu plných buněk

        # Tisk hracího pole
        print(f"""
        {borders}
        |{cells[1]}|{cells[2]}|{cells[3]}|
        {borders}
        |{cells[4]}|{cells[5]}|{cells[6]}|
        {borders}
        |{cells[7]}|{cells[8]}|{cells[9]}|
        {borders}    
            """)
        
        win = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {7, 5, 3}] # Vítězné kombinace

        for k in range(8): # Ověření jestli některý z hráčuů již nevyhrál
            if win[k].intersection(cells_O) == win[k] or win[k].intersection(cells_X) == win[k]:
                if (i % 2 == 1 and j % 2 == 1) or (i % 2 == 0 and j % 2 == 0):
                    print(separator, f"Congratulation, {player_1} WON!!!", separator, sep = "\n")
                    victory = True
                    score_p1 += 1
                    break # Ve velmi vzácném případě by se mohlo vypsat dvakrát
                elif (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
                    print(separator, f"Congratulation, {player_2} WON!!!", separator, sep = "\n")
                    victory = True
                    score_p2 += 1
                    break # Ve velmi vzácném případě by se mohlo vypsat dvakrát
        i += 1 
        if victory:
            break
    else: # Po vyčerpání 9 polí bez výhry se jedná o remízu
        print(separator)
        print("It's a tie, try again!")
        print(separator)
    
    print(f"Score:", f"{player_1}: {score_p1}", f"{player_2}: {score_p2}", separator, sep = "\n") # Výpis skore

    if (endgame := (input("Enter Q to quit the game, any key to repeat the game: ")).upper()) == "Q": # Dalsí hra?
        quit()
    
    else:
        j += 1 
        os.system("cls")