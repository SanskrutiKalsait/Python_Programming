
#Create a Movie class with name and rating. Add a method to check whether the movie rating is good or not.

class Movie:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def check_rating(self):
        if self.rating >= 7:
            print(self.name, "is a good movie")
        else:
            print(self.name, "is not a good movie")


m1 = Movie("Avengers", 8.5)
m1.check_rating()