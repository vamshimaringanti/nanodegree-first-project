class Movie():
    """ This class has information about movies like title, storyline, movie poster, youtube trailer  """

    # constructor to initialize movie instance
    def __init__(self, movie_title, movie_storyline, poster_image, youtube_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
