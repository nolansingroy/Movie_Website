import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story","A story of a boy and his toys",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=ZZv1vki4ou4")
#print(toy_story.storyline)

avatar = media.Movie("Avatar","A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()


xmen = media.Movie("xmen","mutants who fight for the good of humanity",
                   "https://upload.wikimedia.org/wikipedia/en/5/55/X-MenFirstClassMoviePoster.jpg",
                   "https://www.youtube.com/watch?v=kyQKi5-k0UU")
#print(xmen.storyline)
#xmen.show_trailer()

ava = media.Movie("EX Machina","AI Robot Trancends Humanity",
                  "https://resizing.flixster.com/QsOuTEdpjPTIXmQR54Ngzzmi-rQ=/206x305/v1.bTsxMTE5MDkxNjtqOzE3NDU0OzEyMDA7MTM2MDsyMDE1",
                  "https://www.youtube.com/watch?v=XBSYCM1oTNg")
#print(ava.storyline)
#ava.show_trailer()

hp1 = media.Movie("harry potter and the sorcerer's stone", "Journey Beyond your imagination",
                  "https://vignette3.wikia.nocookie.net/harrypotter/images/0/0e/Philostone.jpg/revision/latest?cb=20101208171110"
                  ,"https://www.youtube.com/watch?v=RzCjI3Jy7E8")
print(hp1.storyline)

prometheus = media.Movie("Prometheus", "Two Scientist on the search for the Engineers"
                         ,"https://vignette1.wikia.nocookie.net/avp/images/7/7f/Prometheus_Poster.png/revision/latest?cb=20170125135410"
                         ,"https://www.youtube.com/watch?v=mDqLG28m_Eo")

danceOfReality = media.Movie("La danza de la realidad",
                             "The Dance of Reality reflects Jodorowsky's philosophy that reality is not objective but rather a dance created by our own imaginations.",
                             "http://danceofrealitymovie.com/wp-content/uploads/2014/02/The-Dance-of-Reality-Poster-1000W.jpg",
                             "https://www.youtube.com/watch?v=GMM5tZOsr3Q")
print(prometheus.storyline)
movies = [toy_story, avatar, xmen, ava, hp1, prometheus,danceOfReality]

fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
