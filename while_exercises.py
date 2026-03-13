
# while_exercises.py
# 4.5. while cikla uzdevumi

def input_sum_loop():
    total = 0.0
    while True:
        value = input("Ievadi skaitli vai 'stop': ").strip().lower()
        if value == "stop":
            break
        try:
            total += float(value)
        except ValueError:
            print("Nav skaitlis, mēģini vēlreiz.")
    print(f"Kopējā summa = {total}")

def guessing_game(secret: int = 42, max_tries: int = 7):
    tries = 0
    while tries < max_tries:
        guess_str = input("Mini skaitli: ").strip()
        try:
            guess = int(guess_str)
        except ValueError:
            print("Ievadi veselu skaitli.")
            continue

        if guess == secret:
            print("Pareizi! 🎉")
            return

elif guess < secret:
            print("Par mazu.")
        else:
            print("Par lielu.")
        tries += 1

    print(f"Diemžēl nē. Pareizais skaitlis bija {secret}.")

if __name__ == "__main__":
    print("1) Summa   2) Spēle")
    c = input("Izvēle: ").strip()
    if c == "1":
        input_sum_loop()
    else:
        guessing_game()

