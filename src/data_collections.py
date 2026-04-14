# A daļa
# 1. Saraksts un darbības ar sarakstu

#  --- Sākotnējais saraksts
numbers = [18, 35, 61, 83, 39, 52]
print("--- Saraksti ---")
print (f"Sākotnējais saraksts: {numbers}")

# --- Pievienot elementu beigās
numbers.append(24)
# print(f"Pēc .append(24): {numbers}")

# --- Nodzēst beidzamo elementu
numbers.pop()
# print(f"Pēc .pop(): {numbers}")


# 2. Summa un vidējais
total_sum = 0
count = 0

for num in numbers:
    total_sum += num  # Pieskaitām katru skaitli summai
    count += 1        # Skaitām, cik elementu esam apstrādājuši

average = total_sum / count

print(f"Summa: {total_sum}, Vidējais: {average:.2f}")


# 3. Filtrēšana: tikai pāra skaitļi
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(f"Pāra skaitļi: {even_numbers}")

# 4. Šķēlumi (Slices)
print(f"Pirmie 3: {numbers[:3]}, Pēdējie 2: {numbers[-2:]}")        # Pirmie 3 un pēdējie 2
print(f"Katrs otrais: {numbers[::2]}")                              # Katrs 2. skaitlis


# B daļa
# 1. Vārdnīcas izveide
print("\n--- Vārdnīcas ---")

grades = {
    "Anna": 85,
    "Jānis": 72,
    "Līga": 95,
    "Raitis": 45,
    "Kaspars": 78,
    "Patriks": 83
}
print(f"Sākotnējās atzīmes: {grades}")

# 2. Pievienot studentu, mainīt atzīmi
grades["Kārlis"] = 88               # Pievienojam jaunu studentu
grades["Jānis"] = 80                # Mainām esošā studenta atzīmi 

print(f"Atjaunotā vārdnīca: {grades}")

# 3. Studentu saraksts
print("\n--- Studentu saraksts ---")
for name, grade in grades.items():
    print(f"{name}: {grade}")

# 4. Atrast augstāko atzīmi
top_student = ""
max_grade = -1  # Sākam ar zemāko iespējamo vērtību

for name, grade in grades.items():
    if grade > max_grade:
        max_grade = grade
        top_student = name

print(f"Labākais students: {top_student} ({max_grade})")

# C daļa 
# 1. Pārveidot esošo vārdnīcu par sarakstu ar vārdnīcām
students = []
for name, grade in grades.items():
    students.append({"name": name, "grade": grade})

# 2. Filtrēšana: Atlasīt studentus ar atzīmi >= 80
top_students = []
for ieraksts in students:
    if ieraksts["grade"] >= 80:
        top_students.append(ieraksts)    

# 3. Izvade ar enumerate() un f-strings
print(f"\n--- Studenti ar atzīmi >= 80 ---")

# npk - indekss (sākam no 1), ieraksts - vārdnīca (elements no saraksta)
for npk, ieraksts in enumerate(top_students, start=1):
    print(f"{npk}. {ieraksts['name']} — {ieraksts['grade']}")
