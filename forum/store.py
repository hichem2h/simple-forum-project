class MemberStore:
    members = []

    def add(self, member):
        self.members.append(member)

    def get_all(self):
        return self.members


class PostStore:
    posts = []

    def add(self, post):
        self.posts.append(post)

    def get_all(self):
        return self.posts
