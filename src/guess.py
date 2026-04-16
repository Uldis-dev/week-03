import random
from guess_utils import get_valid_int, ask_yes_no
from guess_logic import check_guess, get_status_message

def play_round():
    """Viens spēles cikls"""
    MIN = 1 
    MAX = 100
    MAX_ATTEMPTS = 10
    merkis = random.randint(MIN, MAX)
    attempts = 0
    
    print(f"\n--- JAUNA SPĒLE ---")
    print(f"Esmu iedomājies skaitli no {MIN} līdz {MAX}. Tev ir {MAX_ATTEMPTS} mēģinājumi.")
    
    while attempts < MAX_ATTEMPTS:
        prompt = f"Mēģinājums {attempts + 1}/{MAX_ATTEMPTS}. Tavs minējums: "
        minejums = get_valid_int(prompt, MIN, MAX)
        attempts += 1
        
        result = check_guess(minejums, merkis)
        
        if result == "correct":
            print(f"Lieliski! Uzminēji skaitli {merkis} ar {attempts}. mēģinājumu.")
            return True
        
        print(get_status_message(result))
        
    print(f"Žēl, bet mēģinājumi beidzās. Mans skaitlis bija {merkis}.")
    return False

def main():
    """Programmas galvenā cilpa."""
    print("Skaitļu minēšanas spēle")
    
    while True:
        play_round()
        if not ask_yes_no("\nVai vēlies spēlēt vēlreiz? (j/n): "):
            print("Paldies par spēli! Uz redzēšanos!")
            break

if __name__ == "__main__":
    main()