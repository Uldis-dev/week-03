def is_email(text):
    if not isinstance(text,str):    # Pārbaude, vai virkne ir teksts
        return False
    
    if "@" in text and "." in text: # Pārbaude, vai satur simbolus '@' un '.'
        if text.startswith("@") or text.endswith("@") or text.endswith("."): # teksts nesākas ar '@' vai nebeidzas ar '@', '.'
            return False
        return True
    
    return False



def is_phone_number(text):
    if not isinstance(text,str):        # Pārbaude, vai virkne ir teksts
        return False

    if not text.startswith("+371 "):        # Pārbaude, vai sākas ar valsts kodu
        return False

    number_part = text[5:]      # Izdalām pašu numuru (daļa pēc '+371 ')
    return len(number_part) == 8 and number_part.isdigit()    # Jābūt tieši 8 cipariem



def is_valid_age(age):
    if not isinstance(age, int):        #Pārbaude, vai ir vesels skaitlis
        return False
    
    return 0 <= age <= 150      # Pārbaude, vai skaitlis ir diapazonā 0-150



def is_strong_password(text):
    if not isinstance(text, str) or len(text) < 8:    # Pārbaude, vai virkne ir teksts un vismaz 8 simbolus garš

    has_digit = False
    for char in text:       # Pārbaude, vai virknē ir kāds cipars
        if char.isdigit():
            has_digit = True
            break  # Tiklīdz atradām vienu ciparu, tālāk meklēt nav jēgas

    has_alpha = False
    for char in text: # Pārbaude, vai virknē ir kāds burts
        if char.isalpha():
            has_alpha = True
            break        

    return has_digit and has_alpha      # Jābūt burtam un ciparam



def is_valid_date(text):
    if not isinstance(text, str) or len(text) != 10:     # Pārbaude, vai virkne ir teksts un tieši 10 simbolus garš
        return False
    
    parts = text.split("-")     # Sadalām pa domuzīmēm: ['2024', '12', '31']
    if len(parts) != 3:         # pārbaudām, vai ir 3 daļas - gads, mēnesis, datums
        return False
        
    
    for part in parts: # Pārbaudām katru daļu atsevišķi, vai ir skaitlis
        if not part.isdigit(): # Ja kaut viena daļa nav skaitlis, viss datums ir nederīgs            
            return False
        
    return True     # Ja izietas visas iepriekšējās pārbaudes, tad datums ir derīgs
    



