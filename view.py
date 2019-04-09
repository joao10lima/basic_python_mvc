def showAllView(list):
    print 'In our db we have %i users. Here they are:' % len(list)
    for item in list:
        print item.full_name


def showContactInfo(list):
    for item in list:
        print item.contact_info()


def startView():
    print 'MVC - the simplest example'
    print ' 1 - See all users on the database'
    print ' 2 - See users contact info'
    print 'Input any other to quit ...'


def endView():
    print 'Invalid option quitting!'
