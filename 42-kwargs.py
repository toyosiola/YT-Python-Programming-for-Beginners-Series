# **kwargs key=value

# def greet_user(name, age):
#   print(f"Hello {name}, you are {age} years old")

# greet_user(age = 12, name = "John")


def print_user_info(name, **kwargs):
    print(name)
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# print_user_info()
def mixed_args(*args, **kwargs):
    print(args)
    print(kwargs)


mixed_args(1, 2, 3, name="Bob", age=20)
