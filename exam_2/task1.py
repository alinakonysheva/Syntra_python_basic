# 1. Maak een programma dat de gebruiker vraagt om zijn leeftijd en naam. Indien de gebruiker
# minstens 18 jaar is vraag dan ook als hij een rijbewijs heeft of niet Als output willen we het
# volgende zien:
# Hallo “naam”, u bent x jaar. U bent A en B.
# A = meerderjarig of minderjarig
# en B = indien ouder dan 65 “en gepensioneerd”.
# Voorbeeld output:
# Hallo Voornaam Familienaam u bent 68 jaar.
# U bent meerderjarig en gepensioneerd.
# U heeft een rijbewijs
# Hallo Voornaam Familienaam u bent 68 jaar.
# U bent meerderjarig en gepensioneerd.
# Hallo Voornaam Familienaam u bent 40 jaar.
# U bent meerderjarig.
# U heeft een rijbewijs
# Hallo Voornaam Familienaam u bent 40 jaar.
# U bent meerderjarig.
# Hallo Voornaam Familienaam u bent 16 jaar.
# U bent minderjarig.
# De gebruiker mag slechts 5x een verkeerde waarde ingeven bij de leeftijd anders stopt het
# programma. Geef een foutmelding dan “U heeft 5 pogingen gehad om een correcte leeftijd in te
# geven, het programma stopt nu”. Gebruik hiervoor een recursieve functie en geen loop !