class MemberStore:
    members = []

    def add(self, member):
        for m in self.members:
            if (member.name == m.name):
                print 'Member {} already exists'.format(member.name)
                return
        self.members.append(member)

    def get_all(self):
        return [m.name for m in self.members]

    def get_by_id(self, id):
        for m in self.members:
            if m.id == id:
                return m.name

    def delete(self, id):
        i = 0
        for m in self.members:
            if m.id == id:
                del self.members[i]
                return
            i += 1

    def entity_exists(self, member):
        return member in self.members

class PostStore:
    posts = []

    def add(self, post):
        self.posts.append(post)

    def get_all(self):
        return [{'title': p.title, 'content': p.content} for p in self.posts]

    def delete(self, post):
        i = 0
        for p in self.posts:
            if p == post:
                del self.posts[i]
                return
            i += 1
