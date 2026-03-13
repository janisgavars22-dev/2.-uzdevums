
# for_exercises.py
# 4.4. for + range uzdevumi

def sum_1_to_n(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def count_even_in_range(a: int, b: int) -> int:
    count = 0
    for x in range(a, b + 1):
        if x % 2 != 0:
            continue
        count += 1

 return count

def fizzbuzz(n: int) -> list[str]:
    out = []
    for i in range(1, n + 1):
        s = ""
        if i % 3 == 0:
            s += "Fizz"
        if i % 5 == 0:
            s += "Buzz"
        out.append(s or str(i))
    return out

if __name__ == "__main__":
    print("Summa 1..10 =", sum_1_to_n(10))
    print("Pāra skaitļu skaits 1..15 =", count_even_in_range(1, 15))
    print("FizzBuzz:", ", ".join(fizzbuzz(16)))

