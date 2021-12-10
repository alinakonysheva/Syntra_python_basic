import json

with open('test_ex.json') as myjsonfile:
    schedule = json.load(myjsonfile)
    print(f"prijs aalst-zav: {schedule['zaventem']['9300']['price']['4']}")
    print(f"prijs aalst-zav - 5 personen: {schedule['zaventem']['9300']['price']['5']}")
    print(f"prijs erpe-mere-charleroi: {schedule['charleroi']['9420']['price']['7']}")