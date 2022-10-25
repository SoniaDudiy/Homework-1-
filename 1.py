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
com4 = Comment('Natalia', 'Mary Poppins', 'Interesting book')
com5 = Comment('Solomia', 'Cinderella', 'Boring book')
com6 = Comment('Olya', 'Harry Potter', 'Exciting book')
com7 = Comment('Arsen', 'Mary Poppins', 'Favorite book')
com8 = Comment('Diana', 'Cinderella', 'Not bad')
com9 = Comment('Jason', 'Harry Potter', 'Engrossing book')
class Book:
    def __init__(self, author, name, year, edition, genre, *comments):
        self.author = author
        self.name = name
        self.year = year
        self.edition = edition
        self.genre = genre
        self.comments = comments

    def print_comments(self):
        comments = ''
        for n, c in enumerate(self.comments, start=1):
            comments += '%d.%s\n' % (n, str(c))
        return comments

    def __eq__(self, other):
        return self.author == other.author and self.name == other.name

    def __repr__(self):
        return '%s_%s_%d' % ('_'.join(self.author.split(' ')), '_'.join(self.name.split(' ')), self.year)

    def __str__(self):
        return '%s - %s(%d).%s edition.\nComments:\n%s ' % (self.author, self.name, self.year,
                                                            self.num(self.edition), self.print_comments())

    def num(self, number):
        num_dict = {
            '1': 'st',
            '2': 'nd',
            '3': 'rd',
            '4': 'th'
        }
        last_digit = str(number)[-1:]
        last_2_digits = str(number)[-2:]
        if 20 >= int(last_2_digits) >= 4:
            return '%s-%s' % (number, num_dict['4'])
        elif int(last_digit) >= 4:
            return '%s-%s' % (number, num_dict['4'])
        else:
            return '%s-%s' % (number, num_dict[last_digit])


book1 = Book("Pamela Lyndon Travers", "Mary Poppins", 1934, 78, "Children's literature", com1, com4, com7)
book2 = Book("Charles Perrault", "Cinderella", 1697, 59, "Fairytale", com2, com5, com8)
book3 = Book("Joanne Rowling", "Harry Potter", 2000, 7, "Fantasy", com3, com6, com9)

print(book1)
print(book2)
print(book3)



