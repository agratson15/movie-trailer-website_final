#By importing media and fresh_tomatoes, we can add our favorite movies here and produce the website

import media
import fresh_tomatoes

#Below you can add your favorite movies with details like, Title, Storyline, Poster Image, Youtube Video, Movie Rating, and Movie Gross
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4",
                        "G",
                        "$191,796,233")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ",
                     "PG-13",
                     "$760,507,625")

dumb_and_dumber = media.Movie("Dumb and Dumber",
                              "Two best friends have a crazy journey across the US",
                              "http://ia.media-imdb.com/images/M/MV5BMTIzNDI5MTc0M15BMl5BanBnXkFtZTYwMjM5NDU5._V1_SX640_SY720_.jpg",
                              "https://www.youtube.com/watch?v=J5pZCQT7JkM",
                              "PG-13",
                              "$127,175,374")

man_of_steel = media.Movie("Man of Steel",
                           "How Superman became man of steel",
                           "http://oyster.ignimgs.com/wordpress/stg.ign.com/2012/12/Man-of-Steel-poster2-610x904.jpg",
                           "www.youtube.com/watch?v=T6DJcgm3wNY",
                           "PG-13",
                           "$291,045,518")

heavyweights = media.Movie("Heavyweights",
                           "A group of overwieght adolecents take over the gamp",
                           "http://images.moviepostershop.com/heavyweights-movie-poster-1995-1020257204.jpg",
                           "www.youtube.com/watch?v=uD4GclR6ZEo",
                           "PG",
                           "$17,689,177")

avengers = media.Movie("The Avengers",
                       "A group of super heros fighting to save the day",
                       "http://ia.media-imdb.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZTcwODg0OTY0Nw@@._V1_SX640_SY720_.jpg",
                       "www.youtube.com/watch?v=eOrNdBpGMv8",
                       "PG-13",
                       "$623,357,910")
#Adding the movies I want on the website and calling to create webpage below.
movies = [toy_story, avatar, dumb_and_dumber, man_of_steel, heavyweights, avengers]
fresh_tomatoes.open_movies_page(movies)

