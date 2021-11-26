
def print_5_times(text: str, counter = 0):
    if counter < 5:
        print('{} - {}'.format(counter+1, text))
        print_5_times(text, counter+1)
        

if __name__ == '__main__':
    print_5_times('mijn tekst')
