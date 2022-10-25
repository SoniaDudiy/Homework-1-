import datetime


class Comment:

    def __init__(self, user, book, comment):
        self.user = user
        self.book = book
        self.date = datetime.date.today()
        self.comment = comment

    def __str__(self):
        return '%s writes about %s : %s. %s.' % (self.user, self.book, self.comment, self.date)

com1 = Comment('Anna', 'Mary Poppins', 'Very bad book')
com2 = Comment('Sofia', 'Cinderella', 'Good')
com3 = Comment('Maksim', 'Harry Potter', 'Favorite book')

book = map(str, input().split())
print (com1)
print (com2)
print (com3)