a = 'ul Jana III SobIESkiego'
b = '\tul. Jana trzeciego Sobieskiego'
c = 'ulicaJana III Sobieskiego'
d = 'UL. JANA 3 \nSOBIESKIEGO'
e = 'UL. jana III SOBiesKIEGO'
f = 'ULICA JANA III SOBIESKIEGO  '
g = 'ULICA. JANA III SOBIeskieGO'
h = ' Jana 3 Sobieskiego  '
i = 'Jana III Sobi\teskiego '

expected = 'Jana III Sobieskiego'

a = a.upper().replace("ULICA","").replace("UL","").replace(".","").replace("TRZECIEGO","III").replace("3","III").replace("\n","").replace("\t","").strip().title().replace("Iii","III")
b = b.upper().replace("ULICA","").replace("UL","").replace(".","").replace("TRZECIEGO","III").replace("3","III").replace("\n","").replace("\t","").strip().title().replace("Iii","III")
c = c.upper().replace("ULICA","").replace("UL","").replace(".","").replace("TRZECIEGO","III").replace("3","III").replace("\n","").replace("\t","").strip().title().replace("Iii","III")
d = d.upper().replace("ULICA","").replace("UL","").replace(".","").replace("TRZECIEGO","III").replace("3","III").replace("\n","").replace("\t","").strip().title().replace("Iii","III")
e = e.upper().replace("ULICA","").replace("UL","").replace(".","").replace("TRZECIEGO","III").replace("3","III").replace("\n","").replace("\t","").strip().title().replace("Iii","III")
f = f.upper().replace("ULICA","").replace("UL","").replace(".","").replace("TRZECIEGO","III").replace("3","III").replace("\n","").replace("\t","").strip().title().replace("Iii","III")
g = g.upper().replace("ULICA","").replace("UL","").replace(".","").replace("TRZECIEGO","III").replace("3","III").replace("\n","").replace("\t","").strip().title().replace("Iii","III")
h = h.upper().replace("ULICA","").replace("UL","").replace(".","").replace("TRZECIEGO","III").replace("3","III").replace("\n","").replace("\t","").strip().title().replace("Iii","III")
i = i.upper().replace("ULICA","").replace("UL","").replace(".","").replace("TRZECIEGO","III").replace("3","III").replace("\n","").replace("\t","").strip().title().replace("Iii","III")

print(f"{a == expected}\t \"{a}\"")
print(f"{b == expected}\t \"{b}\"")
print(f"{c == expected}\t \"{c}\"")
print(f"{d == expected}\t \"{d}\"")
print(f"{e == expected}\t \"{e}\"")
print(f"{f == expected}\t \"{f}\"")
print(f"{g == expected}\t \"{g}\"")
print(f"{h == expected}\t \"{h}\"")
print(f"{i == expected}\t \"{i}\"")

