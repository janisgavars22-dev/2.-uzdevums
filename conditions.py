
# conditions.py
# 4.3. Nosacījumi, loģiskie operatori, ievades validācija

def get_discount_category(age: int, is_student: bool) -> str:
    if age < 7 or age >= 65:
        return "bez maksas"
    elif is_student or (7 <= age <= 17):
        return "50% atlaide"
    else:
        return "pilna cena"

if __name__ == "__main__":
    name = input("Ievadi vārdu: ").strip()

    age_str = input("Ievadi vecumu (skaitlis): ").strip()
    try:
        age = int(age_str)
    except ValueError:
        print("Kļūda: vecumam jābūt veselam skaitlim.")
        exit(1)

    student_raw = input("Vai esi students? (jā/nē): ").strip().lower()
    is_student = student_raw in ("jā", "ja", "yes", "y", "1", "true")

    category = get_discount_category(age, is_student)
    needs_id = is_student and not (age < 7 or age >= 65)

    print(f"{name}, tava kategorija: {category}")
    if needs_id:
        print("Lūdzu, uzrādi derīgu ISIC.")
