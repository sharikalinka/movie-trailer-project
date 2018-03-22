import webbrowser

class Movie():

    """ Class that represents a movie """

    def __init__(self, title, year, poster_url, trailer_url):
        """ Initializes a Movie object 
        Arguments:
        title = movie's title string
        year =  year of the movie's release integer
        poster_url = URL to a poster image string
        trailer_url = YouTube movie trailer URL string
        """
        self.title = title
        self.year = year
        self.poster_url = poster_url
        self.trailer_url = trailer_url

    def show_trailer():
        """ Open trailer in web browser """
        webbrowser.open(self.trailer_url)