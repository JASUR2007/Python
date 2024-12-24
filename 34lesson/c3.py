class Movie:
    def __init__(self, title, genre, rating=0):
        self.title = title
        self.genre = genre
        self.__rating = rating
    def setRating(self, rating):
        if rating >= 1 and rating <= 10:
            self.__rating = rating
        else:
            print('ERROR')
    def getInfo(self):
        return f'Title: {self.title}\nGenre: {self.genre}\nRating: {self.__rating}'
    
movie = Movie('Sidjin', 'Horror')
movie.setRating(8)
print(movie.getInfo())