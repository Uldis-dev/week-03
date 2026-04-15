def is_email(text):
    """
	Pārbauda vai teksta virkne ir derīga e-pasta adrese
	- satur '@' un '.'
	- nesākas ar '@' un nebeidzas ar '@' vai '.'

	Args:
	text(str): Apstrādājamā teksta virkne - epasta adrese
	
	Returns:
	bool: True/False
	
	Example:
	>>> is_email('anna@inbox.lv')
	True
	>>> is_email('anna')
	False
	>>> is_email('anna@inbox.')
	False
	"""    
    
    if not isinstance(text,str):    # Pārbaude, vai virkne ir teksts
        return False
    
    if "@" in text and "." in text: # Pārbaude, vai satur simbolus '@' un '.'
        if text.startswith("@") or text.endswith("@") or text.endswith("."): # teksts nesākas ar '@' vai nebeidzas ar '@', '.'
            return False
        return True
    
    return False



def is_phone_number(text):
    """
    Pārbauda vai ievadītais teksts atbilst Latvijas telefona numura formātam: +371 XXXXXXXX (8 cipari)
	
	Args:
	text(str): Apstrādājamā teksta virkne - telefona numurs
	
	Returns:
	bool: True/False

	Example:
	>>> is_phone_number('+371 26123456')
	True
	>>> is_phone_number('26123456')
	False
	>>> is_phone_number('+371 2612345')
	False
    """

    if not isinstance(text,str):  # Pārbaude, vai virkne ir teksts
        return False

    if not text.startswith("+371 "):        # Pārbaude, vai sākas ar valsts kodu
        return False

    number_part = text[5:]      # Izdalām pašu numuru (daļa pēc '+371 ')
    return len(number_part) == 8 and number_part.isdigit()    # Jābūt tieši 8 cipariem



def is_valid_age(age):
    """
	Pārbauda vai ievadītais veselais skaitlis atbilst vecums (robežās 0-150)
	
	Args:
	age(int): Vecums veselos skaitļos
		
	Returns:
	bool: True/False

	Example:
	>>> is_valid_age('desmit')
	False
	>>> is_valid_age('10g')
	False
	>>> is_valid_age(10)
	True
	>>> is_valid_age(-10)
	False
    """
     
    if not isinstance(age, int):        #Pārbaude, vai ir vesels skaitlis
        return False
    
    return 0 <= age <= 150      # Pārbaude, vai skaitlis ir diapazonā 0-150



def is_strong_password(text):
    """
	Pārbauda vai ievadītais teksts ir droša parole:
	- vismaz 8 simboli
	- satur burtus un ciparus
	
	Args:
	text(str): Apstrādājamā teksta virkne - parole
	
	Returns:
	bool: True/False

	Example:
	>>> is_strong_password('1234')
	False
	>>> is_strong_password('12345678')
	False
	>>> is_strong_password('1234567a')
	True
    """

    if not isinstance(text, str) or len(text) < 8:    # Pārbaude, vai virkne ir teksts un vismaz 8 simbolus garš
        return False
    
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
    """
	Pārbauda vai ievadītais teksts atbilst datuma formātam YYYY-MM-DD 
	
	Args:
	text(str): Apstrādājamā teksta virkne - datums
	
	Returns:
	bool: True/False

	Example:
	>>> is_valid_date('2026-26-aprīlis')
	False
	>>> is_valid_date('26.04.2026')
	False
	>>> is_valid_date('2026-04-26')
	True
    """

    if not isinstance(text, str) or len(text) != 10:     # Pārbaude, vai virkne ir teksts un tieši 10 simbolus garš
        return False
    
    parts = text.split("-")     # Sadalām pa domuzīmēm: ['2024', '12', '31']
    if len(parts) != 3:         # pārbaudām, vai ir 3 daļas - gads, mēnesis, datums
        return False
        
    
    for part in parts: # Pārbaudām katru daļu atsevišķi, vai ir skaitlis
        if not part.isdigit(): # Ja kaut viena daļa nav skaitlis, viss datums ir nederīgs            
            return False
        
    return True     # Ja izietas visas iepriekšējās pārbaudes, tad datums ir derīgs


