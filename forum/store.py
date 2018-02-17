class MemberStore:
    members = []
    last_id = 1

    def add(self, member):
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    def get_all(self):
        return self.members

    def get_by_id(self, id):
        result = None
        all_members = self.get_all()
        for e in all_members:
            if e.id == id :
                result = e
                break
        return result

    def entity_exists(self, member):
        result = False
        if self.get_by_id(member.id) is not None:
            result = True
            break
        return result

    def delete(self, id):
        member = self.get_by_id(id)
        MemberStore.members.remove(member)


class PostStore:
    posts = []

    def add(self, post):
        self.posts.append(post)

    def get_all(self):
        return self.posts
