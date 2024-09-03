def add_numbers(num1, num2):
    return num1 + num2
print(add_numbers(1,2))  ## print is for outcome view only


def is_even(number):
    return number % 2 == 0
print(is_even(8))   ## print is for outcome view only


def reverse_string(text):
    return text[::-1]
print(reverse_string(text='stanley'))  ## print is for outcome view only


def count_vowels(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)
print(count_vowels(text='count'))   ## print is for outcome view only


def calculate_factorial(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
print(calculate_factorial(5))   ## print is for outcome view only


def apply_decorator(func):
    def decorator_func(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return decorator_func

## print is for outcome view only
def greet():
    return "Hello!"
decorated_greet = apply_decorator(greet)
print(decorated_greet())


def sort_by_age(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])

    ## print is for outcome view only
people = [("Frank", 30), ("Don", 25), ("Stanley", 35)]
print(sort_by_age(people))


def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict

## print is for outcome view only
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge_dicts(dict1, dict2)) 


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Information: {self.year} {self.make} {self.model}")

        ## print is for outcome view only
my_car = Car(make="Porche", model="Cayennee", year="2024")
my_car.display_info() 