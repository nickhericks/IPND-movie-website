import webbrowser


class Movie():
    """This class provides a way to store movie related information.

    Args:
        param1: self
    Behavior:
        Creates space in memory for every instance passed through.
    Returns:
        The return value. True for success, False otherwise.
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """Initialize instance of class Movie.

        Args:
            param1: movie_title
            param2: movie_storyline
            param3: poster_image
            param4: trailer_youtube
        Behavior:
            Takes in instance of Movie and assigns variables to each argument.
        Returns:
            The return value. True for success, False otherwise.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Play trailer for instance of class Movie.

        Args:
            param1: trailer_youtube_url
        Behavior:
            Open url in browser tab.
        Returns:
            The return value. True for success, False otherwise.
        """
        webbrowser.open(self.trailer_youtube_url)
