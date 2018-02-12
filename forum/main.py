import models

member1 = models.Member('Hichem', 21)
member2 = models.Member('Ahmed', 43)

print member1.name, member1.age
print member2.name, member2.age

post1 = models.Post('Title 01', 'Some Content in the 1st post of the 1MAC forum')
post2 = models.Post('Title 02', 'Some Content in the 2nd post of the 1MAC forum')
post3 = models.Post('Title 03', 'Some Content in the 3rd post of the 1MAC forum')

print post1.title, post1.content
print post2.title, post2.content
print post3.title, post3.content
