def get_valid_int(prompt, min_val, max_val):
    """
    Prasa lietotājam ievadīt veselu skaitli noteiktā diapazonā. Turpina prasīt, kamēr tiek ievadīts derīgs skaitlis.
    """
    while True:
        try:
            ievade = input(prompt)
            skaitlis = int(ievade)
            
            if min_val <= skaitlis <= max_val:
                return skaitlis
            
            print(f"Kļūda: Skaitlim jābūt robežās no {min_val} līdz {max_val}!")
        except ValueError:
            print("Kļūda: Lūdzu, ievadi derīgu veselu skaitli!")

def ask_yes_no(prompt):
    """
    Pārbauda, vai lietotājs vēlas turpināt (atgriež True/False).
    """
    atbilde = input(prompt).lower().strip()
    return atbilde == 'j'