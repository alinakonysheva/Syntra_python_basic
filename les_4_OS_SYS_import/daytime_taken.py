from datetime import datetime, timedelta

# Maak een programma dat het volgende afdrukt: Vandaag zijn we: datum
# Morgen zijn we: datum
# Gisteren waren we: datum
# Volgend jaar zijn we het jaar X

today = datetime.now()
tomorrow = today + timedelta(days=+1)
yesterday = today + timedelta(days=-1)
nextyear = today.year + 1
nextyear = datetime(today.year+1, today.month, today.day)
print(f'Vandaag is {today.strftime("%m/%d/%Y")}\nGisteren is {yesterday.strftime("%m/%d/%Y")},\nVolgend jaar is\
{nextyear.strftime("%Y")}')

# Maak een programma dat de geboortedatum van de gebruiker vraagt. Druk het volgende af - zijn geboortedatum inclusief de naam van de dag in het Nederlands
# voorbeeld: uw geboortedatum is “2/9/1979”, dit was op een zondag
# - wanneer hij 18 jaar is geworden en de naam van de dag in het Nederlands
# voorbeeld: u was 18 jaar op datum, dit was op een xxxxx (dag van de week in het Nederlands) - zijn huidige leeftijd
# voorbeeld: u bent nu x aantal jaar oud)
# - wanneer hij op pensioen mag gaan (67 jaar, maand nadien)
# voorbeeld: u mag in “maand” in het “jaar” op pensioen gaan (maand in het Nederlands zetten)

day_of_birth = int(input('Geeft uw geborte dag '))
day_of_month = int(input('Geeft uw geborte maand '))
day_of_year = int(input('Geeft uw geborte jaar '))

s = day_of_year + day_of_month + day_of_birth
date = datetime(year=int(s[0:4]), month=int(s[4:6]), day=int(s[6:8]))