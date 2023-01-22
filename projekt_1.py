"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jan Jankula
email: JanJankula@gmail.com
discord: Honza J.#3020

"""

# Vstupný text, z kterého budeme vybírat textové stringy.
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
         '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
         '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# ÚVOD 1: Vstupní uvítání a vstupní paramentry
vstupy = {"Bob": "123", "Ann": "pass123", "Mike": "password123", "Liz": "pass123"}
uvitani = "$ python projekt1.py"
mezera = 40 * '-'
print(uvitani.upper())

# Zadaní vstupných údajů: jmeno a heslo
#                          - vyhodnocení zda se jméno a heslo shodují
#                          - zamítnutí vstupu pří nesplění podmínky 
jmeno = input("username: ")
heslo = input("password: ")
if vstupy.get(jmeno) != heslo:
    print("unregistered user, terminating the program..".upper())
    quit()

# ÚVOD 2: Po zadaní správných údajů  - uvítání přihlášeného a výběr čísla textu na analýzu
#                                    - nahlášení chyba, pokud se zadá namísto čísla písmeno a nebo jiné než definované číslo
statistika = len(TEXTS)
print(mezera)
print(f"Welcome to the app, {jmeno}.")
print("We have 3 texts to be analyzed.")
print(mezera)
moznosti = input("Enter a number btw. 1 and 3 to select: ")

if moznosti.isalpha():
    print(mezera)
    print("Nie je zadané číslo!".upper())
    print(mezera)
    quit()
elif (int(moznosti)-1) not in range(3):
    print(mezera)
    print("Wrong number entered!".upper())
    print(mezera)
    quit()

    # Hlavní programu 1. část: :počet slov, počet slov začínajících velkým písmenem,
#                       - počet slov psaných velkými písmeny, počet slov psaných malými písmeny,
#                       - počet čísel (ne cifer),bsumu všech čísel (ne cifer) v textu

else:
    text = TEXTS[int(moznosti)-1]
    neupravene_slova = text.split()
    slova = []

    for slovo in neupravene_slova:
        slovo = slovo.strip(".,?:!;|/'")
        if slovo: slova.append(slovo)

    titlecase = 0
    uppercase = 0
    lowercase = 0
    numeric = 0
    numeric_suma = 0
    pocty_pismen = {}

    for slovo in slova:
        if slovo.istitle():
            titlecase += 1
        elif slovo.isupper():
            uppercase += 1
        elif slovo.islower():
            lowercase += 1
        elif slovo.isdigit():
            numeric += 1
            numeric_suma += int(slovo)

# Hlavní programu 2. část rozdelení slov v textu podle kategorie délky
#                       - uspořádání slov podle kategorie délky
        l = len(slovo)
        pocty_pismen[l] = pocty_pismen.setdefault(l, 0)+1
    usporadani_pocty = sorted(pocty_pismen)

# Ukončení programu 1. část: vypsání počtu slov v texte
#                           - vypsání počtu slov podle přerozdělení do jednotlivých kategorií
#                           - vypsání celkového počtu číslic v textu
    print(mezera)
    print(f"There are {len(slova)} words in the selected text.")
    print(f"There are {titlecase} titlecase words.")
    print(f"There are {uppercase} uppercase words.")
    print(f"There are {lowercase} lowercase words.")
    print(f"There are {numeric} numeric strings.")
    print(f"The sum of all the numbers {numeric_suma}")
    print(mezera)

# Ukončení programu 2. část:
#   -  vytvoření  hlavičky sloupcového grafu popisujícího uspořádání počtu slov podle délky
    print(f"LEN |{'OCCURENCES': ^24}| NR.")
    hlavicka = len("LEN")

#   - vytvoření cyklu, který generuje sloupcový graf
    for i in usporadani_pocty:
        delka = pocty_pismen[i]
        print(f"{' ' * (hlavicka - len(str(i))) + str(i): ^3} | {'*' * delka +  ' '* (22 - delka)} | {delka}")