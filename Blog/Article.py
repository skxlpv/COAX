from Blog.Singleton import singleton


@singleton
class Article:
    def __init__(self, title, description, author, date):
        self.title = title
        self.description = description
        self.author = author
        self.date = date
