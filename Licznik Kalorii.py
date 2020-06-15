print("Cześć tu Python.Jak masz na imię?")
imię=input().strip()
print("Więc witam Cię",imię+".\nMiło Cię poznać.")
print("Ile masz lat?",imię+".")
wiek=int(input().strip())
print("W wieku",wiek,"lat ile masz wzrostu w cm?")
wzrost=int(input().strip())
print("I przy wzroście",wzrost,"cm ile masz wagi w kg?")
waga=int(input().strip())
print("A tak się Ciebie spytam",imię,"jaką masz płeć?\nJesteś mężczyzną czy kobietą?")
płeć=input().strip()
if płeć == "kobieta":
    płeć2 = -161
if płeć == "mężczyzna":
    płeć2 = 5
print("Czyli",imię,"przy wzroście",wzrost,"cm i wadzę",waga,"kg i w wieku",wiek,"lat to Twoje zpotrzebowanie kaloryczne wynosi: {:.0f} kalorii na dobę." .format((waga*10)+(wzrost*6.25)-(wiek*5)-płeć2))
print("A gdybym wiedział jak bardzo masz ciężką pracę to podałbym Ci dokładne Twoje zapotrzebowanie klaoryczne.\nPodaj liczbę odpowiadającą Twojemu dziennemu wysiłkowi:\nWysiłek bardzo lekki, lekki, umiarkowany, ciężki czy bardzo ciężki?")
wysiłek=input().strip()
if wysiłek == "bardzo lekki":
    wysiłek2 = float(1.2)
if wysiłek == "lekki":
    wysiłek2 = float(1.4)
if wysiłek == "umiarkowany":
    wysiłek2 = float(1.6)
if wysiłek == "ciężki":
    wysiłek2 = float(1.8)
if wysiłek == "bardzo ciężki":
    wysiłek2 = float(2)
print("Znając jaki wysiłek dziennie podejmujesz to Twoje zapotrzebowanie kaloryczne to {:.0f} kalorii na dobę." .format(((waga*10)+(wzrost*6.25)-(wiek*5)-płeć2)*wysiłek2))





