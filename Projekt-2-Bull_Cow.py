"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: David Herman
email: david.herman@seznam.cz
discord: DavidHerman#5014
"""
import random
import pickle
import os
from timeit import default_timer as timer

if not os.path.isfile("Bull-Cow_stats.dat"): # Kontrola zda je přítomen soubor pro zapisování sttistiky, pokud ne je vytvořen
    
    stats = {}
    with open("Bull-Cow_stats.dat", "wb") as st:
        pickle.dump(stats, st)
    
with open("Bull-Cow_stats.dat", "rb") as st:    # Otevření souboru se statistikou her
    stats = pickle.load(st)
    
separator = "-" * 75
i = 1   # Počítadlo pokusů
secret = str(random.randint(1023, 9876)) # Generování náhodného čísla

while len(set(secret)) != 4: # Ověření, že se ve vygenerovaném čísle neopakuje číslice 
    secret = str(random.randint(1023, 9876))

while (name := input("Enter your name: ").title()) in stats.keys(): # Ověření jestli už někdo s tímto jménem hru hrál
    print("Someone with that name has already played the game, is that you?")
    if (yes_no := input("'Y' for Yes or any key for No: ").upper()) != "Y":
        print("You have to use a different name")
    elif yes_no == "Y":
        break
    
# Uvítání a pravidla
print(separator)
print(f"Hi {name}!")
print(separator)
print("""
I've generated a random 4 digit for you. No digit is repeated and 
the first digit is not zero.
      
bull - corect digit in correct place, cow - correct digit in wrong place.
      
Let's play a bulls and cows game.
""")
print(separator)
start = timer()
while (tip := input("Enter a 4 digit number: ")) != secret: # Tip od uživatele
       
    while not tip.isnumeric() or len(tip) != 4 or len(set(tip)) != 4 or int(tip[0]) == 0:   # Ověření že vložené číslo má čtyři číslice a nezačíná nulou
        print("""
            Remember you must enter a 4 digit number without 
            repeating digits and the first one is not zero!
            """)
        tip = input("Enter a 4 digit number: ")
    
    if tip == secret: # Jinak by při prvním zadáném neplatném vstupu nebylo při správně uhodnutém číslu vyhodnoceno jako výhra 
        break

    i += 1  # Přičtení pokusu v počítadle
    bulls = 0   # Vynulování počítadel 
    cows = 0    # Vynulování počítadel

    for index in range(4):  # Vyhodnocení správně uhodnutých číslic
        if tip[index] == secret[index]:
            bulls += 1
        elif tip[index] in secret:
            cows += 1
    
    if bulls == 1 and cows == 1:    # Použití množného či jednotného čísla
        print(f"{bulls} bull, {cows} cow")
    elif bulls == 1 and cows != 1:
        print(f"{bulls} bull, {cows} cows")
    elif bulls != 1 and cows == 1:
        print(f"{bulls} bulls, {cows} cow")
    else:
        print(f"{bulls} bulls, {cows} cows")
    print(separator)

end = timer()
elapsed_time = round(((end - start) / 60), 1)
print(separator)
if i == 1:  # Vyhodnocení hry
    print(f"""
Incredible, you guessed it the first time and in time {elapsed_time} min!
    """)
elif i < 10:
    print(f"""
Congratulations, you just guessed the right number in {i} guesses and
in time {elapsed_time} min!
    """)
else:
    print(f"""
You should train more, you just guessed the right number in {i} guesses and 
in time {elapsed_time} min! 
    """)
    
if name in stats.keys():    # Statistika
    stats[name]["count"].append(i) # Přidání právě dosažených výsledků do proměnné pro výpočet statistických parametrů
    stats[name]["time"].append(elapsed_time)
    mean_tips = sum(stats[name]["count"]) / int(len(stats[name]["count"]))  # Výpopčet průměrů
    mean_time = sum(stats[name]["time"]) / int(len(stats[name]["time"]))
    min_tips = min(stats[name]["count"])    # Vyhledání minimálních hodnot
    min_time = min(stats[name]["time"])
    print(f"Your mean is {round(mean_tips, 1)} tips per game in mean time {round(mean_time, 1)} min.")
    print(f"Your best time is {min_time} min and the smallest number of tips is {min_tips}.")

else:
    print("This is your first game")
    stats.update({name: {"count": [i], "time": [elapsed_time]}})

with open("Bull-Cow_stats.dat", "wb") as st: # Uložení statistiky do souboru
    pickle.dump(stats, st)
print(separator)