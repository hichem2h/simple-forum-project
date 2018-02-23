from datetime import datetime

class Post:
    def __init__ (self, title, content, member_id = 0):
        self.title = title
        self.content = content
        self.id = 0
        self.member_id = member_id
        self.date = datetime.now()

    def __str__ (self):
        return 'member_id: {}, title :{},content: {}, id: {}'.format(self.member_id, self.title, self.content, self.id)

class Member:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        self.id = 0
        self.posts = []

    def __str__ (self):
        return 'name :{}, age :{}, id: {}, posts: {}'.format(self.name, self.age, self.id, self.posts)
