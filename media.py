import webbrowser

#create class Movie
class Movie():
    """
    Class Movie has a constructor with title, storyline, poster, trailer, director of the movie.
    And it has a function show_trailer.
    """
    def __init__(self, title, storyline, poster, trailer, director):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        self.director = director
    #function that open the webbrowser to the specified URL
    def show_trailer(self):
        webbrowser.open(self.trailer_url)
