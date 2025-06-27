def do_twice (p):
    p()
    p()

def print_spam():
    print('spam')
do_twice(print_spam)
