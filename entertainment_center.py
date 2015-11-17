import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story",
                        "The toys are alive, and they love Andy",
                        "http://aforismi.meglio.it/img/film/Toy_story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "John Lasseter")
avatar = media.Movie("Avatar",
                     "Blue aliens hate pink aliens, they have good reasons",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "James Cameron")
interstellar = media.Movie("Interstellar",
                        "A man go in space trying to save humanity",
                        "https://lh5.googleusercontent.com/-_LZCNOpWcfI/AAAAAAAAAAI/AAAAAAAAAAA/SEQ-XjwXhlU/s0-c-k-no-ns/photo.jpg",
                        "https://www.youtube.com/watch?v=zSWdZVtXT7E",
                        "Christopher Nolan")
gladiator = media.Movie("Gladiator",
                        "A General become a gladiator",
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=IvTT29cavKo",
                        "Ridley Scott")
cloud_atlas = media.Movie("Cloud Atlas",
                        "Different people in different time trying to be free",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcQZQhasO56in_vxYDa30rB9tzQg1wk6yKJkkdVoxG43hCJeYuEm",
                        "https://www.youtube.com/watch?v=hWnAqFyaQ5s",
                        "Lana Wachowski, Andy Wachowski, Tom Tykwer")
gran_torino = media.Movie("Gran Torino",
                        "An old man and his Gran Torino",
                        "http://www.gstatic.com/tv/thumb/movieposters/183329/p183329_p_v7_ab.jpg",
                        "https://www.youtube.com/watch?v=9ecW-d-CBPc",
                        "Clint Eastwood")
movies = [toy_story, avatar, interstellar, gladiator, cloud_atlas, gran_torino]
fresh_tomatoes.open_movies_page(movies)
