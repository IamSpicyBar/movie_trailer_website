import webbrowser


class Movie():
    """A model of a movie"""

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """Initialize title, storyline,
        poster_image_url, and trailer_youtube_url attributes"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Show trailer of the movie"""
        webbrower.open(self.trailer_youtube_url)
