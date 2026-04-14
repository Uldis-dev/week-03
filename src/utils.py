def capitalize(text):
    """
    Pārveido teksta pirmo burtu par lielo, pārējos par mazajiem.

    Args:
    text (str): Apstrādājamā teksta virkne.

    Returns:
    str: Virkne ar lielo sākumburtu.

    Example:
    >>> capitalize("hello WORLD") 
    "Hello world"
    """
        
    # 1. Validācija
    if not isinstance(text, str):
        raise TypeError("Ievadei jābūt teksta virknei!")
    
    if text == "":
        return ""

    # 2. Loģika: pirmais burts lielais + pārējie mazie
    return text[0].upper() + text[1:].lower()

def truncate(text, max_len=20):
    """
    Apgriež tekstu līdz norādītajam garumam.
	
	Args:
    text (str): Apstrādājamā teksta virkne.
	max_len (int): Līdz kādam garumam apgriezt tekstu (def=20)
	
	Returns:
	str: Līdz noteiktajam garumam apgriezta teksta virkne
	
	Example:
    >>> truncate("Hello, world, nice d")
	"Hello, world, nice d"
	>>> truncate("Hello, world, nice day today!", 18)
	"Hello, world, nice"
    """

    # 1. Validācija
    if not isinstance(text, str):
        raise TypeError("Ievadei jābūt teksta virknei!")

    # 2. Loģika: atgriezt pirmos max_len simbolus no teksta virknes  
    return text[:max_len] 

def count_words(text):
    """
    Saskaita vārdu skaitu tekstā, ignorējot liekās atstarpes.

    Args:
    text (str): Apstrādājamā teksta virkne.

    Returns:
    int: Vārdu skaits teksta virknē

    Example:
    >>> count_words("Sveika,   pasaule!")
	2
	>>> count_words("Hello, world, nice day today!")
	5
    """

    # 1. Validācija
    if not isinstance(text, str):
        raise TypeError("Ievadei jābūt teksta virknei!")   

    # 2. Loģika: atgriezt vārdu skaitu teksta virknē
    words = text.split()    
    return len(words)

def clamp(num, low, high):
    """
    Ierobežo skaitli noteiktā diapazonā [low, high].

    Args:
    num (int, float): Skaitlis, kuru pārbaudīt.
    low (int, float): Apakšējā robeža.
    high (int, float): Augšējā robeža.

    Returns:
    int, float: Ierobežotā vērtība.
    
    Example:
    >>> clamp(150, 0, 100)
	100
    >>> clamp(-10, 0, 100)
	0
    """

    # 1. Validācija
    if not isinstance(num, (int, float)):
        raise TypeError("Pirmajam parametram 'num' jābūt skaitlim!")
        
    if not isinstance(low, (int, float)):
        raise TypeError("Parametram 'low' jābūt skaitlim!")
        
    if not isinstance(high, (int, float)):
        raise TypeError("Parametram 'high' jābūt skaitlim!")      
    
    # 2. Pārbaude, vai diapazons ir loģisks
    if low > high:
        raise ValueError("Kļūda: 'low' nevar būt lielāks par 'high'!")    

    # 3. Paša 'clamp' loģika
    if num < low:
        return low
    if num > high:
        return high
    
    return num        

def is_prime(num):
    """
    Pārbauda, vai skaitlis ir pirmskaitlis.
	
	Args:
    num (int): Vesels skaitlis (lielāks par 1), kuru pārbaudīt
	
	Returns:
	bool: True, ja ir pirmskaitlis, citādi False.
	
	Example:
	>>> is_prime(10)
	False
	>>> is_prime(7)
	True
    """	

    # 1. Validācija 
    if not isinstance(num, int):
        raise TypeError("Pirmskaitļu pārbaudei jāizmanto vesels skaitlis!")    
    
    # 2. Skaitļi mazāki par 2 nav pirmskaitļi
    if num < 2:
        return False
    
    # 3. Pārbaude ar ciklu
    # Sākam no 2 un pārbaudām visus skaitļus līdz mūsu skaitlim
    i = 2
    while i < num:
        if num % i == 0:
            # Ja dalās bez atlikuma, tas nav pirmskaitlis
            return False
        i += 1
    
    # Ja neviens dalītājs neatradās, tas ir pirmskaitlis
    return True
    
def factorial(n):
    """
    Aprēķina skaitļa n faktoriālu (n!).
    
    Args:
    n (int): Vesels skaitlis, kas nav mazāks par 0.
    
    Returns:
    int: Faktoriāla vērtība.
    
    Example:
    >>> factorial(5)
	120
    """	

    # 1. Validācija 
    if not isinstance(n, int):
        raise TypeError("Faktoriālu var aprēķināt tikai veselam skaitlim!")
    
    if n < 0:
        raise ValueError("Faktoriālu nevar aprēķināt negatīvam skaitlim!")    
    
    if n > 100:
        raise ValueError("Skaitlis ir pārāk liels! Drošības robeža ir 100.")
    
    # 2. Aprēķināšana ar ciklu
    result = 1
    
    # range(1, n + 1) nodrošina, ka cikls iet no 1 līdz n ieskaitot
    for i in range(1, n + 1):
        result *= i  # Tas pats, kas: result = result * i
        
    return result


def total(numbers):
    """
    Aprēķina skaitļu saraksta kopējo summu, neizmantojot iebūvēto sum().
    
    Args:
    numbers (list): Saraksts ar veseliem skaitļiem vai skaitļiem ar komatu.
    
    Returns:
    float/int: Visu elementu summa.
    
    Example:
    >>> total ([10, 20, 30])
	60
	>>> total ([1.5, 2.5, 10.0])
	14.0
    """

    # 1. Validācija: vai ievade ir saraksts
    if not isinstance(numbers, list):
        raise TypeError("Funkcijai jānodod saraksts (list)!")
    
    # 2. Cikls iet cauri katram elementam
    result = 0
    
    for num in numbers:
        # Pārbaudām, vai katrs elements sarakstā ir skaitlis
        if not isinstance(num, (int, float)):
            raise ValueError(f"Sarakstā atrasts nederīgs elements: {num}. Drīkst būt tikai skaitļi.")
            
        result += num  # Pieskaitām pašreizējo skaitli kopsummai
        
    return result

def average(numbers):
    """
    Aprēķina skaitļu saraksta vidējo aritmētisko vērtību.
    
    Args:
    numbers (list): Saraksts ar veseliem skaitļiem vai skaitļiem ar komatu.
    
    Returns:
    float: Vidējā vērtība vai 0.0, ja saraksts ir tukšs.
	
	Example:
	>>> average ([10, 20, 30])
	20.00
	>>> Average ([1.5, 2.5, 10.0])
	4.67
    """	
        
    # 1. Validācija: vai ievade ir saraksts
    if not isinstance(numbers, list):
        raise TypeError("Funkcijai jānodod saraksts (list)!")
    
    # 2. Speciālais gadījums: tukšs saraksts
    # Ja saraksts ir tukšs, len() būs 0. Dalīt ar 0 nedrīkst.
    if len(numbers) == 0:
        return 0.0
    
    # 2. Cikls iet cauri katram elementam
    total_sum = 0
    count = 0
    
    for num in numbers:
        # Pārbaudām, vai katrs elements sarakstā ir skaitlis
        if not isinstance(num, (int, float)):
            raise ValueError(f"Sarakstā atrasts nederīgs elements: {num}. Drīkst būt tikai skaitļi.")
            
        total_sum += num  # Pieskaitām katru skaitli summai
        count += 1        # Skaitām, cik elementu esam apstrādājuši
        
    return total_sum / count     



if __name__ == "__main__":
    # Šeit testējam funkcijas
    testa_teksts = "hello, WORLD, nICE dAY TodAY! "
    
    print("--- Virkņu funkciju testēšana ---")
    print(f"Ievade: {testa_teksts}")

    print(f"\nCapitalize: {capitalize(testa_teksts)}")
    print(f"Truncate 19: {truncate(testa_teksts,19)}")
    print(f"Count words: {count_words(testa_teksts)}")  

    print("\n--- Skaitļu funkciju testēšana ---") 
    print(f"Clamp (10, 20, 100): {clamp(10, 20, 100)}")

    print(f"Is prime 10: {is_prime(10)}")
    print(f"Is prime 7: {is_prime(7)}")

    print(f"Factorial 5: {factorial(5)}")


    print("\n--- Saraksta funkciju testēšana ---")    

    # Tests (veseli skaitļi)
    paraugs1 = [10, 20, 30]
    print(f"Total ({paraugs1}): {total(paraugs1)}")
    print(f"Average ({paraugs1}): {average(paraugs1):.2f}")

    # Tests ar decimālskaitļiem (float)
    paraugs2 = [1.5, 2.5, 10.0]
    print(f"\nTotal ({paraugs2}): {total(paraugs2)}")
    print(f"Average ({paraugs2}): {average(paraugs2):.2f}")

    # Tukšs saraksts
    paraugs3 = []
    print(f"\nTotal ({paraugs3}): {total(paraugs3)}")
    print(f"Average ({paraugs3}): {average(paraugs3):.2f}")

    # Kļūdu apstrādes tests (try-except bloks)
    paraugs4 = ["čau", 5]
    try:
        total(paraugs4) # Šim vajadzētu izsaukt ValueError
        print(f"\nTotal ({paraugs4}): {total(paraugs4)}")
    except ValueError as e:
        print(f"\nTotal ({paraugs4}): Noķerta plānotā kļūda: {e}")

    try:
        average(paraugs4) # Šim vajadzētu izsaukt ValueError
        print(f"Average ({paraugs4}): {average(paraugs4):.2f}")
    except ValueError as e:
        print(f"Average ({paraugs4}): Noķerta plānotā kļūda: {e}")    