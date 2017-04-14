import webbrowser
import json
import urllib

# Making a class with search in DB omdbapi by title
class Movie():
    def __init__(self, movie_title, trailer_youtube_url):
        connect = urllib.urlopen("http://www.omdbapi.com/?t=" + movie_title)
        movie_info = json.loads(connect.read())

        self.title = movie_info['Title']
        self.storyline = movie_info['Plot']
        self.poster_image_url = movie_info['Poster']
        self.trailer_youtube_url = trailer_youtube_url
        self.runtime = movie_info['Runtime']
        self.genre = movie_info['Genre']

# Open window with trailer-url
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
