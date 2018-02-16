class Post:
    def __init__ (self, title, content):
        self.title = title
        self.content = content

class Member:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def __str__ (self):
        return 'name :{}, age :{}, id: {}'.format(self.name, self.age, self.id)
