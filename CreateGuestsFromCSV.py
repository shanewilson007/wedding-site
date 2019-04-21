import csv


# Run script in production terminal after importing User object
def CreateUser():
    guests = [i.strip() for i in open('guest.txt').readlines()]
    for guest in guests:
        first, space, last = guest.partition(' ')
        last = last.split()
        last = last[0]
        username = (first+'.'+last)
        user = User(
                username=username,
                first_name=first,
                last_name=last,
        )
        user.set_password('UserPassword')
        user.save()
