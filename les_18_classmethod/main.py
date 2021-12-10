from song import create_songlist, print_songlist, add_song, remove_song, play_song, most_played
from inputs import get_input_item


def main_menu() -> int:
    print('-'*30)
    print('mogelijkheden')
    print('1. songs bekijken')
    print('2. song toevoegen')
    print('3. song wissen')
    print('4. song afspelen')
    print('5. meest afgespeeld')
    print('6. stopppen')
    return get_input_item('geef uw keuze: ', 1)
    

def main_loop(songs: list):
    if songs is not None:
        choice = 1
        while choice in [1, 2, 3, 4, 5]:
            choice = main_menu()
            if choice == 1:
                print_songlist(songs)
            elif choice == 2:
                add_song(songs)
            elif choice == 3:
                remove_song(songs)
            elif choice == 4:
                play_song(songs)
            elif choice == 5:
                most_played(songs)

        songs.save()


def main():
    songs = create_songlist()
    main_loop(songs)

  
if __name__ == '__main__':
    main()