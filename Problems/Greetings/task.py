def morning(func_name):
    def wrapper(name):
        func_name(name)
        print("Good morning,", name)
    return wrapper

