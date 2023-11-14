"""Importing from other modules"""

from lessons import my_functions

if __name__ == "__main__":
    print("howdy!")
    



"""Things I'll be importing"""

def addition(x: int, y: int):
    return x + y

my_variable: str = "Hello!"

if __name__ == "__main__":
    print("this should only print when running my functions")
else:
    print("my_functions is being imported")