import media
import fresh_tomatoes
# Info to search in DB by Title
snatch = media.Movie('Snatch',
                        'https://www.youtube.com/watch?v=ni4tEtuTccc')

lstsb = media.Movie('Lock, Stock and Two Smoking Barrels',
                     'https://www.youtube.com/watch?v=WoZ2kTlwKTk')

bronx_tale = media.Movie('Bronx Tale',
                         'https://www.youtube.com/watch?v=H_lijLYuw-o')

batman_dk = media.Movie('The Dark Knight',
                         'https://www.youtube.com/watch?v=EXeTwQWrcwY')

batman_b = media.Movie('Batman Begins',
                         'https://www.youtube.com/watch?v=neY2xVmOfUM')

batman_dkr = media.Movie("The Dark Knight Rises",
                         'https://www.youtube.com/watch?v=g8evyE9TuYk')
deep_sea = media.Movie("Deep blue sea",
                        'https://www.youtube.com/watch?v=GCs2slK8GkY')
terminator = media.Movie('Terminator 2',
                        'https://www.youtube.com/watch?v=HgV7-MJwUBw')
hangover = media.Movie('The Hangover',
                        'https://www.youtube.com/watch?v=tcdUhdOlz9M')
# list of all films
movies = [snatch, lstsb, batman_dk, batman_b, batman_dkr, bronx_tale,
            deep_sea, terminator, hangover]
# Make html file with all films
fresh_tomatoes.open_movies_page(movies)
