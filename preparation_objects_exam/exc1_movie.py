from movie import create_movielist, print_movies, add_movie
from inputs import get_input_item


def main_menu() -> int:
    print('-'*30)
    print('mogelijkheden')
    print('1. film uit lijst kiezen')
    print('2. film toevoegen')
    print('3. stopppen')
    return get_input_item('geef uw keuze: ', 1)
    

def main_loop(movies: list):
    if movies is not None:
        choice = 1
        while choice in [1, 2]:
            choice = main_menu()
            if choice == 1:
                print_movies(movies)
            elif choice == 2:
                add_movie(movies)
            else:
                movies.save()


def main():
    movies = create_movielist()
    main_loop(movies)

  
if __name__ == '__main__':
    main()