import media
import fresh_tomatoes
"""
Documentation for entertainment_center.py:
Each movie object is an instantiation of media.Movie() , which can be found in
media.py. Please read media.py for information on the parameters!
Uses an Array object "movie" to store the objects and the function
open_movies_page() imported from fresh_tomatoes.py
"""

"""
Birdman object ...
"""
birdman = media.Movie(
    "Birdman",
    "the unexpected virtue of ignorance",
    "http://bit.do/birdman_pep8",
    "https://www.youtube.com/watch?v=E7Bap9gv7hY")
# print(birdman.storyline)

"""
Ava object ...
"""
ava = media.Movie("Ex Machina",
                  "AI Robot Trancends Humanity",
                  "http://bit.do/ExMachina2",
                  "https://www.youtube.com/watch?v=XBSYCM1oTNg")
# print(ava.storyline)
# ava.show_trailer()

"""
hp1 object ...
"""
hp1 = media.Movie("Harry Potter And The Philosopher's Stone",
                  "Journey Beyond your imagination",
                  "http://bit.do/HarryPotter_pep8",
                  "https://www.youtube.com/watch?v=RzCjI3Jy7E8")
# print(hp1.storyline)

"""
Prometheus Object ...
"""
prometheus = media.Movie("Prometheus",
                         "Two Scientist on the search for the Engineers",
                         "http://bit.do/prometheus_pep8",
                         "https://www.youtube.com/watch?v=mDqLG28m_Eo")
# print(prometheus.storyline)

"""
Endless Peotry Object
"""
endlessPoetry = media.Movie(
    "Endless Poetry",
    "Alejandro Jodorowsky recounts his young adulthood in Chile.",
    "http://bit.do/endlesspoetry_pep8",
    "https://www.youtube.com/watch?v=4L3_510gM-U")
"""
Dune Object
"""
dune = media.Movie("Dune",
                   "The Greatest Film that was never made!",
                   "http://bit.do/dune_pep8",
                   "https://www.youtube.com/watch?v=m0cJNR8HEw0")
"""
Dance of Reality Object
"""
danceOfReality = media.Movie(
    "La danza de la realidad",
    "Jodorowsky's idea that reality is created by our own imaginations.",
    "http://bit.do/danceofreality_pep8",
    "https://www.youtube.com/watch?v=GMM5tZOsr3Q")
# print(danceOfReality.storyline)

"""
Array to hold all of the objects
"""
movies = [birdman, ava, hp1, prometheus, danceOfReality,
          endlessPoetry, dune]
"""
Dynamically create an html from the movies array object
using the function open_movie_page() passing in an array as a parameter
"""
fresh_tomatoes.open_movies_page(movies)

print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
