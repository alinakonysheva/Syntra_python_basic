# Maak een programma dat urls kan opslaan van producten op Amazon.
# Ga dan de prijs op zoeken. Voorzie ook dat er meerdere url’s kunnen worden opgeslagen.
# Zo kan je de prijs vergelijken op Amazon in Duitsland, Amazon in Nederland en Amazon in Frankrijk
# Voeg nu toe om bijvoorbeeld hetzelfde product op te zoeken bij bol of coolblue.

import requests
import bs4 as bs

headers = (
{'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
 'Accept-Language': 'en-US, en;q=0.5'})

response = requests.get('https://www.amazon.fr/Fitbit-Sense-Lunar-White-Unisex-Adult/dp/B08DFLG5SP/ref=sr_1_1_sspa?crid=11UC0EDU57FM8&keywords=fitbit%2Bsense%2B4&qid=1642761719&sprefix=Fitbit%2Bsen%2Caps%2C87&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTE5VUlRCRE1DTFVXJmVuY3J5cHRlZElkPUEwNzc4NzE0M0lMSDAzSVFFSkFJJmVuY3J5cHRlZEFkSWQ9QTAxODAzMzUyVjNCVlUySVNRM0RXJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1',
    headers=headers)
print(response)
print(response.status_code)

html = response.content

soup = bs.BeautifulSoup(html, 'lxml')

el = soup.find_all("span", {"class": "a-offscreen"})[0]

print(el)


"""soup = bs.BeautifulSoup(html, 'lxml')
print(soup)
l = soup.find_all("div", {"class": "cms-content hide@sm-down"})
for item in l:
    print(item)
    print('---------')
    print(item.text)
"""