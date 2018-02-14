import models, store

ms = store.MemberStore()
ps = store.PostStore()

member1 = models.Member('Hichem', 21, 0)
member2 = models.Member('Ahmed', 43, 1)

ms.add(member1)
ms.add(member2)
ms.add(member1)

print ms.get_all()
print ms.get_by_id(0)
print ms.entity_exists(member2)
ms.delete(1)
print ms.entity_exists(member2)

post1 = models.Post('Title 01', 'Some Content in the 1st post of the 1MAC forum', 0)
post2 = models.Post('Title 02', 'Some Content in the 2nd post of the 1MAC forum', 1)
post3 = models.Post('Title 03', 'Some Content in the 3rd post of the 1MAC forum', 2)

ps.add(post1)
ps.add(post2)
ps.add(post3)

print ps.get_all()
