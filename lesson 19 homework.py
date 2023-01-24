def debug(func):
    def wrapper(name, age=None):
        print(func.__name__, name, age)
        return func(name, age)
    return wrapper


@debug
def greeting(name, age=None):
    if age:
        return f"Hi {name} your age is {age} ".format(name=name, age=age)
    else:
        return f"Hi, {name}!".format(name=name)


print(greeting("Миша"))
print(greeting("Паша", age=100))
print(greeting(name="Саша", age=16))



