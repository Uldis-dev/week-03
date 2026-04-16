import random

while True:  # Ārējais cikls - spēles atkārtošanai
    # Ģenerējam jaunu skaitli katrai spēlei
    MINAMAIS_SKAITLIS = random.randint(1, 100)
    MEGINAJUMU_SKAITS = 0
    MAX_MEGINAJUMU_SKAITS = 10
    UZMINETS = False

    print(f"\nEsmu iedomājies skaitli no 1 līdz 100. Tev ir {MAX_MEGINAJUMU_SKAITS} mēģinājumi.")

    while MEGINAJUMU_SKAITS < MAX_MEGINAJUMU_SKAITS:
        IEVADE = input(f"Mēģinājums {MEGINAJUMU_SKAITS + 1}/{MAX_MEGINAJUMU_SKAITS}. Tavs minējums: ")

        # --- Pārbaudām, vai ievade ir skaitlis
        try:
            MINEJUMS = int(IEVADE)
        except ValueError:
            print("Kļūda: Lūdzu, ievadi veselu skaitli!")
            continue  # Atgriežas uz cikla sākumu, neskaitot šo kā mēģinājumu

        # --- Pārbaudām vai skaitlis ir vajadzīgajā diapazonā
        if not (1 <= MINEJUMS <= 100):
            print("Minējums ir ārpus spēles robežām (1-100)!")
            continue # Atgriežas uz cikla sākumu, neskaitot šo kā mēģinājumu

        # --- Pieskaitām derīgu mēģinājumu
        MEGINAJUMU_SKAITS += 1

        # --- Pārbaudām minējumu
        if MINEJUMS < MINAMAIS_SKAITLIS:
            print("Par mazu!")
        elif MINEJUMS > MINAMAIS_SKAITLIS:
            print("Par lielu!")
        else:
            UZMINETS = True
            break  # Uzminēts! Lecam ārā no iekšējā cikla

# --- Spēles beigu paziņojumi ---
    if UZMINETS:
        print(f"Apsveicu! Tu uzminēji skaitli {MINAMAIS_SKAITLIS} ar {MEGINAJUMU_SKAITS}. mēģinājumu.")
    else:
        print(f"Diemžēl mēģinājumi beidzās. Mans iedomātais skaitlis bija {MINAMAIS_SKAITLIS}.")        

# --- Vai spēlēt vēlreiz?
    VELREIZ = input("\nVai vēlies spēlēt vēlreiz? (j/n): ").lower().strip()
    if VELREIZ != 'j':
        print("Paldies par spēli! Atā!")
        break  # Iziet no ārējā cikla un beidz programmu