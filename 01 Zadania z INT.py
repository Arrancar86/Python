Name = "Kamil"  # "This is my name"

print(f"Hello World {Name}")

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
WORKDAY = 8 * HOUR
WORKWEEK = 40 * HOUR
WORKMONTH = 22 * WORKDAY


print(f"5 minut to {MINUTE*5} sekund.")
print(f"1 godzina to {HOUR} sekund.")
print(f"Dzień pracy to {WORKDAY} sekund.")
print(f"Tydzień pracy to {WORKWEEK} sekund.")
print(f"Miesiąc pracy to {WORKMONTH} sekund.")

b = 1
Kb = 1024 * b
Mb = 1024 * Kb
B = 8*b
KB = 1024*B
MB = 1024*KB
Link = 100 * Mb
File = 100 *MB
print(f"Czas pobrania to {round(File/Link)} sekund.")

C = 0
K= C - 273
DAYMOONC = 180 + C
DAYMOONK = 180 + K
NIGHTMOONC = 93 + C
NIGHTMOONK = 93 + K
MARSMEDIUMC = -63 + C
MARSMEDIUMK = -63 + K
MARSHIGHC = 20 + C
MARSHIGHK = 20 + K
MARSLOWC = 120 + C
MARSLOWK = 120 + K

print(f"W dzień temperatura na księżycu to {DAYMOONC} C i {DAYMOONK} K.")
print(f"Nocą temperatura na księżycu to {NIGHTMOONC} C i {NIGHTMOONK} K.")
print(f"Średnia temperatura na marsie to {MARSMEDIUMC} C i {MARSMEDIUMK} K.")
print(f"Najwyższa temperatura na marsie to {MARSHIGHC} C i {MARSHIGHK} K.")
print(f"Najniższa temperatura na marsie to {MARSLOWC} C i {MARSLOWK} K.")
