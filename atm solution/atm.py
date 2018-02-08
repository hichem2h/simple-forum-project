def receive(request, money):
    cash = [100, 50, 20, 10, 5, 2, 1]
    if money < request:
        refuse(money)
    else :
        remainder = money - request
        for e in cash:
            while request >= e:
                give (e)
                request -= e
        finish(remainder)

def give(bill):
    print 'Give: ' + str(bill)

def refuse(money):
    print 'Request refused (not enough money): ' + str(money) + ' available'

def finish(remainder):
    print 'Request Finished: '  + str(remainder) + ' available'
