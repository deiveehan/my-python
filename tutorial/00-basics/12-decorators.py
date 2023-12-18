def track(func):
    def wrapper():
        print("-> Entering " )
        func()
        print("<- Exiting ")
    return wrapper


@track
def sayhi():
    print("Say hello to my friend Ruban")


sayhi()
