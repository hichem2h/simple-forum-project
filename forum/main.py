import models, store


ms = store.MemberStore()
ps = store.PostStore()

def create_member_instances():
    member1 = models.Member('Hichem', 21)
    member2 = models.Member('Ahmed', 43)
    print 'Members created'
    return member1, member2

def create_post_instances():
    post1 = models.Post('Title 01', 'Some Content in the 1st post of the 1MAC forum')
    post2 = models.Post('Title 02', 'Some Content in the 2nd post of the 1MAC forum')
    post3 = models.Post('Title 03', 'Some Content in the 3rd post of the 1MAC forum')
    print 'Posts created'
    return post1, post2, post3

def add_instances_to_stores(instances, store):
    for instance in instances:
        store.add(instance)
    print 'Instances added to stores'

def print_all_members(member_store):
    print("=" * 30)
    for member in member_store.get_all():
        print(member)
    print("=" * 30)

member_instances = create_member_instances()
member1, member2 = member_instances
add_instances_to_stores(member_instances, ms)
print_all_members(ms)
