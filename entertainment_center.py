import fresh_tomatoes
import media

fellowship_of_ring = media.Movie("The Lord of the Rings: The Fellowship of the Ring",
                                 "A group on a journey to destroy a evil ring",
                                 "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
                                 "https://www.youtube.com/watch?v=V75dMMIW2B4")

two_towers = media.Movie("The Lord of the Rings: The Two Towers",
                         "The story continues and a war is prepared",
                         "https://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg",
                         "https://www.youtube.com/watch?v=LbfMDwc4azU")

return_of_king = media.Movie("The Lord of the Rings: The Return of the King",
                             "A great battle with extrordinary pictures and motions",
                             "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",
                             "https://www.youtube.com/watch?v=r5X-hFf6Bwo")

farewell_concubine = media.Movie("Farewell My Concubine",
                                 "Two male stars' life in a Peking opera troupe",
                                 "https://upload.wikimedia.org/wikipedia/en/c/c5/Farewell_My_Concubine_poster.jpg",
                                 "https://www.youtube.com/watch?v=cC-_SLiRnJE")

attorney = media.Movie("The Attorney",
                       "A lawyer fights for students tortured by government power",
                       "https://upload.wikimedia.org/wikipedia/en/b/b5/The_Attorney_poster.jpg",
                       "https://www.youtube.com/watch?v=QDaG0IF7ucc")

departures = media.Movie ("Departures",
                          "Story about a traditional Japanese ritual mortician",
                          "https://upload.wikimedia.org/wikipedia/en/e/e1/Okuribito_%282008%29.jpg",
                          "https://www.youtube.com/watch?v=6UFlWO5zhO8")

movies = [fellowship_of_ring, two_towers, return_of_king, farewell_concubine, attorney, departures]
fresh_tomatoes.open_movies_page(movies)
