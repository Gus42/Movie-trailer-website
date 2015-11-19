import media
import fresh_tomatoes

# Creating some objects of type Movie,
# in which are stored data relating to movies.
# Each instance of a Movie will have:
# 1- The title of the movie
# 2- A short storyline of the movie
# 3- An URL to the poster image of the movie
# 4- An URL to the trailer, in youtube, of the movie
# 5- The name/s of the director/s of the movie
toy_story = media.Movie("Toy Story",
                        "The toys are alive, and they love Andy",
                        "http://aforismi.meglio.it/img/film/Toy_story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "John Lasseter")
avatar = media.Movie("Avatar",
                     "Blue aliens hate pink aliens, they have good reasons",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd"
                     +"8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "James Cameron")
interstellar = media.Movie("Interstellar",
                        "A man go in space trying to save humanity",
                        "https://lh5.googleusercontent.com/-_LZCNOpWcfI/AAAAAAA"
                        +"AAAI/AAAAAAAAAAA/SEQ-XjwXhlU/s0-c-k-no-ns/photo.jpg",
                        "https://www.youtube.com/watch?v=zSWdZVtXT7E",
                        "Christopher Nolan")
gladiator = media.Movie("Gladiator",
                        "A General become a gladiator",
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/"
                        +"Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=IvTT29cavKo",
                        "Ridley Scott")
cloud_atlas = media.Movie("Cloud Atlas",
                        "Different people in different time trying to be free",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcQZQhas"
                        +"O56in_vxYDa30rB9tzQg1wk6yKJkkdVoxG43hCJeYuEm",
                        "https://www.youtube.com/watch?v=hWnAqFyaQ5s",
                        "Lana Wachowski, Andy Wachowski, Tom Tykwer")
gran_torino = media.Movie("Gran Torino",
                        "An old man and his Gran Torino",
                        "http://www.gstatic.com/tv/thumb/movieposters/"
                        +"183329/p183329_p_v7_ab.jpg",
                        "https://www.youtube.com/watch?v=9ecW-d-CBPc",
                        "Clint Eastwood")

# Store the instances of Movie in a list
movies = [toy_story, avatar, interstellar, gladiator, cloud_atlas, gran_torino]
# Call the open_movies_page function of fresh_tomatoes.py.
# It will take the list of movies, and it will generate a web page to show them.
fresh_tomatoes.open_movies_page(movies)
