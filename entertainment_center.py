import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story",
                        "Toys are live",
                        "",
                        "")
avatar = media.Movie("Avatar","Blue aliens","http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp","https://www.youtube.com/watch?v=5PSNL1qE6VY")

movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
