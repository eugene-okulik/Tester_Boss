def finish_me(func):

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("finished")

    return wrapper


@finish_me
def my_func():
    print("print me")


my_func()
