# Maak een programma dat elke seconde de tijd afdrukt en dit gedurende 60 seconden
from datetime import datetime
import time

C_TIME_REPEAT = 60
C_TIME_ASLEEP = 1

for i in range(0, C_TIME_REPEAT):
    print(i, datetime.now())
    time.sleep(C_TIME_ASLEEP)
