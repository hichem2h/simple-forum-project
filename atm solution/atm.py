def receive(request, money):
    cash = [100, 50, 20, 10, 5, 2, 1]
    if money < request:
        refuse(money)
    elif request < 0 :
        print 'Request should be more than zero'
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

if __name__ == '__main__':
    receive(-188, 200)
