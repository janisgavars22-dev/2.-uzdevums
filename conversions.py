
# conversions.py
# 4.2. Konstantes, konversijas, aritmētika un f-string formatēšana

PI = 3.1415926535
KM_IN_MILE = 1.609344
SEC_IN_MIN = 60

def km_to_miles(km: float) -> float:
    return km / KM_IN_MILE

def miles_to_km(miles: float) -> float:
    return miles * KM_IN_MILE

def c_to_f(c: float) -> float:
    return c * 9/5 + 32

def circle_area(radius: float) -> float:
    return PI * (radius ** 2)

if __name__ == "__main__":
    km = 10
    miles = km_to_miles(km)
    print(f"{km} km = {miles:.2f} mi")

    r = 3.5
    area = circle_area(r)
    print(f"Aplim ar r={r} laukums = {area:.3f}")

    c = 21.5
    print(f"{c}°C = {c_to_f(c):.1f}°F")

    total_seconds = 5 * SEC_IN_MIN + 42
    print(f"5 min 42 s = {total_seconds} s")
