def bingo(fn):

    def whatever():
        print("before")
        fn()
        print("after")

    return whatever

@bingo
def say_hello():
    print("hello from scaler")

say_hello()
