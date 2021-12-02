from constants import C_STOP



def get_input(text : str) -> any:
    return input(text).lower().strip()


condition = True
while condition:
   
    if get_input('mijn test') == C_STOP:
        condition = False
        continue

