import fresh_tomatoes
import media


"""Identify instances of class Movie."""

royal = media.Movie("The Royal Tenenbaums",
                    """An estranged family of former child prodigies reunites
                    when their father announces he is terminally ill.""",
                    "http://www.iceposter.com/thumbs/MOV_0060743c_b.jpg",
                    "https://www.youtube.com/watch?v=2L4lLc_9Hgw")

tom_petty = media.Movie("Runnin' Down A Dream",
                        """Directed by cinema legend Peter Bogdanovich, is
                        the story of one of America's great rock and roll
                        bands told as never before.""",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/6/6f/Runninhomepage.jpg/220px-Runninhomepage.jpg",  # noqa
                        "https://www.youtube.com/watch?v=bGnG3Wh11kY")

almost_famous = media.Movie("Almost Famous",
                            """A high-school boy is given the chance to write
                            a story for Rolling Stone Magazine about an
                            up-and-coming rock band as he accompanies them
                            on their concert tour.""",
                            "https://upload.wikimedia.org/wikipedia/en/d/dd/Almost_famous_poster1.jpg",  # noqa
                            "https://www.youtube.com/watch?v=6iyp0qcf7-w")

interstellar = media.Movie("Interstellar",
                           """A team of explorers travel through a
                           wormhole in space in an attempt to ensure
                           humanity's survival.""", "http://www.hollywoodreporter.com/sites/default/files/custom/Blog_Images/interstellar3.jpg",  # noqa
                           "https://www.youtube.com/watch?v=nyc6RJEEe0U")

brother = media.Movie("Oh Brother Where Art Thou",
                      """A modern satire loosely based on Homer's
                      epic poem, Odyssey.""",
                      "https://upload.wikimedia.org/wikipedia/en/5/5b/O_brother_where_art_thou_ver1.jpg",  # noqa
                      "https://www.youtube.com/watch?v=kID9iXY5Nuk")

wild = media.Movie("Into The Wild",
                   """After graduating from Emory University, top student
                   and athlete Christopher McCandless abandons his
                   possessions, gives his entire $24,000 savings
                   account to charity and hitchhikes to Alaska to
                   live in the wilderness.""",
                   "https://upload.wikimedia.org/wikipedia/en/8/8a/Into-the-wild.jpg",  # noqa
                   "https://www.youtube.com/watch?v=2LAuzT_x8Ek")

movies = [royal, almost_famous, tom_petty, interstellar, brother, wild]

fresh_tomatoes.open_movies_page(movies)
