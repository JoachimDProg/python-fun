# a function is defined using the def keyword
# the value the function expects is called a parameter
# default parameters can be assigned in the method signature
def hello(fname='colonel', mname='', lname='sanders'):
    print(f"Hello {fname.title()} {lname.title()}!")

# function with return
def hello2(fname='colonel', mname='', lname='sanders'):
    return {'fname': fname, 'mname': mname, 'lname': lname}


# the value passed into the function call is called an argument
hello("bobby", '', "boucher")

# keyword arguments are a name-pair value that is associated with the parameter name
# even if the arguments are not in the correct order, they will be correctly associated
print("\nreversed arguments")
hello("vaillancourt", "vicky")
print("reversed arguments with keywords")
hello(lname="vaillancourt", fname="vicky")

# default values can be defined for each parameters
print("\ndefault arguments")
hello()

# return a dictionary from function
print("\nreturn dictionary")
print(hello2('jon', 'bon', 'jovi'))

# function with return
def add(a, b):
    return a + b

total = add(2, 3)
print(f"\nfunction with return value: add 2+3 = {total}")

# lambda function
def sub_lambda(a, b): return a - b


print(f"\nlambda function with return value: sub 8-5 = {sub_lambda(8, 5)}")

# arbitrary parameters: can send any number of arguments, a tuple will be sent to the function
def fill_game_shelf(*games):
    for game in games:
        print(f"\t{game}")


print("\narbitrary parameters \nmy games")
fill_game_shelf('final fantasy vii', 'metal gear solid', 'chocobo racing', 'resident evil 2')

# arbitrary keywords parameters: can send any number of key-value arguments, a dictionary will be sent to the function
def console_games(console, **games):
    print(f"my console: {console}")
    for game, name in games.items():
        print(f"\t{game}: {name}")


print("\narbitrary parameters")
console_games('playstation')
print("\narbitrary keywords parameters")
console_games('playstation', game1='final fantasy vii', game2='metal gear solid', game3='chocobo racing')
