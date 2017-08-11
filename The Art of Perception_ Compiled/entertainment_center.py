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
birdman = media.Movie("Birdman",
                      "the unexpected virtue of ignorance",
                      "http://expatspost.com/wp-content/uploads/1-BIRDMAN-poster2.jpg",
                      "https://www.youtube.com/watch?v=E7Bap9gv7hY")
#print(birdman.storyline)

"""
Ava object ...
"""
ava = media.Movie("Ex Machina","AI Robot Trancends Humanity",
                  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUxNzc0OTIxMV5BMl5BanBnXkFtZTgwNDI3NzU2NDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                  "https://www.youtube.com/watch?v=XBSYCM1oTNg")
#print(ava.storyline)
#ava.show_trailer()

"""
hp1 object ...
"""
hp1 = media.Movie("Harry Potter And The Philosopher's Stone", "Journey Beyond your imagination",
                  "https://vignette3.wikia.nocookie.net/harrypotter/images/0/0e/Philostone.jpg/revision/latest?cb=20101208171110"
                  ,"https://www.youtube.com/watch?v=RzCjI3Jy7E8")
#print(hp1.storyline)

"""
Prometheus Object ...
"""
prometheus = media.Movie("Prometheus", "Two Scientist on the search for the Engineers"
                         ,"https://vignette1.wikia.nocookie.net/avp/images/7/7f/Prometheus_Poster.png/revision/latest?cb=20170125135410"
                         ,"https://www.youtube.com/watch?v=mDqLG28m_Eo")
#print(prometheus.storyline)

"""
Endless Peotry Object
"""
endlessPoetry = media.Movie("Endless Poetry",
                            "Alejandro Jodorowsky recounts his young adulthood in a bohemian Santiago de Chile and his breakthrough as a poet.",
                            "http://t3.gstatic.com/images?q=tbn:ANd9GcQD5oockguxW9sBvaWaVy_Z1IoyqhRtxvfwTdIIBYLZKm_txqS_",
                            "https://www.youtube.com/watch?v=suyruCTA2I4")
"""
Dune Object
"""
dune = media.Movie("Dune",
                   "The Greatest Film that was never made!",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU0MzcxMTAxMl5BMl5BanBnXkFtZTgwODMyMTIxMTE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                   "https://www.youtube.com/watch?v=m0cJNR8HEw0")
"""
Dance of Reality Object
"""
danceOfReality = media.Movie("La danza de la realidad",
                             "The Dance of Reality reflects Jodorowsky's philosophy that reality is not objective but rather a dance created by our own imaginations.",
                             "http://danceofrealitymovie.com/wp-content/uploads/2014/02/The-Dance-of-Reality-Poster-1000W.jpg",
                             "https://www.youtube.com/watch?v=GMM5tZOsr3Q")
#print(danceOfReality.storyline)

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
