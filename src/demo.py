# 1. Importējam nepieciešamos moduļus
#from utils import capitalize, truncate, count_words, clamp, is_prime, factorial, total, average
#from validators import is_email, is_phone_number, is_valid_age, is_strong_password, is_valid_date

import utils
import validators

# --- utils.py funkciju testēšana ---
print("=== UTILS.PY TESTI ===")

# Teksta funkcijas
t1 = "hello WORLD"
print(f"capitalize('{t1}') : '{utils.capitalize(t1)}'")

t2 = "Hello, world, nice day today!"
print(f"truncate('{t2}', 18) : '{utils.truncate(t2, 18)}'")

t3 = "Sveika,    pasaule!"
print(f"count_words('{t3}') : {utils.count_words(t3)}")

# Skaitļu funkcijas
n1 = 150
print(f"clamp({n1}, 0, 100) : {utils.clamp(n1, 0, 100)}")

n2 = -10
print(f"clamp({n2}, 0, 100) : {utils.clamp(n2, 0, 100)}")

n3 = 7
print(f"is_prime({n3}) : {utils.is_prime(n3)}")

n4 = 5
print(f"factorial({n4}) : {utils.factorial(n4)}")

# Sarakstu funkcijas
s1 = [10, 20, 30]
print(f"total({s1}) : {utils.total(s1)}")

s2 = [1.5, 2.5, 10.0]
print(f"average({s2}) : {utils.average(s2):.2f}")


# --- validators.py funkciju testēšana ---
print("\n=== VALIDATORS.PY TESTI ===")

# E-pasts
e1 = 'anna@inbox.lv'
e2 = 'anna@inbox.'
print(f"is_email('{e1}') : {validators.is_email(e1)}")
print(f"is_email('{e2}') : {validators.is_email(e2)}")

# Telefona numurs
ph1 = '+371 26123456'
ph2 = '26123456'
print(f"is_phone_number('{ph1}') : {validators.is_phone_number(ph1)}")
print(f"is_phone_number('{ph2}') : {validators.is_phone_number(ph2)}")

# Vecums
v1 = 10
v2 = -10
print(f"is_valid_age({v1}) : {validators.is_valid_age(v1)}")
print(f"is_valid_age({v2}) : {validators.is_valid_age(v2)}")

# Parole
ps1 = '12345678'
ps2 = '1234567a'
print(f"is_strong_password('{ps1}') : {validators.is_strong_password(ps1)}")
print(f"is_strong_password('{ps2}') : {validators.is_strong_password(ps2)}")

# Datums
d1 = '2026-04-26'
d2 = '26.04.2026'
print(f"is_valid_date('{d1}') : {validators.is_valid_date(d1)}")
print(f"is_valid_date('{d2}') : {validators.is_valid_date(d2)}")