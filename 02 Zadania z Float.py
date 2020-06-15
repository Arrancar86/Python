altitude = 10000
bottle = 20
speed = 75

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE

M = 1
KM = 1000 * M
FT = 0.3048 * M
MI = 1609.344 * M
NMI = 1852 * M
KPH = KM / HOUR
MPH = MI / HOUR

LITER = 1
FLOZ = 0.02957344 * LITER

print(f"Limit prędkości wynosi {round((speed*MI)/KM,1)} km/h.")
print(f"Wysokość przelotowa samolotu wynosi {round (altitude * FT,1)} metrów.")
print(f"Butelka ma {round(bottle * FLOZ,2)} litrów.")

m = 1337

print(f'Meters: {m}')
print(f'Kilometers: {m/KM}')
print(f'Miles: {round(m/MI,2)}')
print(f'Nautical Miles: {round(m/NMI,3)}')
print(f'All: m: {m}, km: {m/KM}, mi: {round(m/MI,2)}, nm: {round(m/NMI,3)}')

Pa =1
hPa =100 * Pa
kPa = 10 * hPa
psi =6894.757 * Pa

EMU = 4.3 * psi
ORLAN = 400 * hPa

print(f"Skafander EMU posiada ciśnienie operacyjne wynoszące - {round(EMU/kPa,2)} kPa oraz {round(EMU/psi,2)} psi.")
print(f"Skafander ORLAN posiada ciśnienie operacyjne wynoszące - {round(ORLAN/kPa,2)} kPa oraz {round(ORLAN/psi,2)} psi.")

Ata = 1013.25 * hPa
Atmosphere = 1013.25 * hPa
Nitrogen = 78.084
Oxygen = 20.946
Argon = 0.9340
CarbonD = 0.0407
Others = 0.001

print("1.Standardowa atmosfera to",round(Atmosphere/hPa,2),"hPa.")
Oxygen2 = (Atmosphere * Oxygen)/100
print("2.Ciśnienie tlenu nad poziomem morza wynosi",round(Oxygen2/hPa,2),"hPa.")

Gradient = 11.3 *Pa / 1*M
DeathBorder = ((Atmosphere-Oxygen2)/Gradient)

print(f"3.Ciśnienie atmosferyczne jest równe ciśnieniu parcjalnemu tlenu na wyskości: {round(DeathBorder,2)} metrów nad poziomem morza.")

