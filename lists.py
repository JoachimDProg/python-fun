# list: uses [], items are ordered, changeable and allow duplicates
consoles = ["ps1", "ps2", "n64", "gameboy"]
print(f"print list: {consoles}")
print(f"print last item: list[-1]: {consoles[-1]}\n")

# append() adds an elenemts to the end
consoles.append('switch')
print(f"add item: list.append('item'): {consoles}\n")

# insert() adds item at specific index
consoles.insert(2, 'ps3')
print(f"insert item: list.insert(pos, 'item':): {consoles}\n")

# del deletes an item at specific index
del consoles[4]
print(f"delete item: del list[pos]: {consoles}\n")

# pop() will return an item by index, default is last
# python uses underscore for variables naming instead of camel casing
popped_console = consoles.pop(4)
print(f"pop item: list.pop(pos): {popped_console}\n")

# remove() removes the last item
consoles.remove("n64")
print(f"remove item: list.remote('value'): {consoles}\n")

# refill list
consoles.append('switch')
consoles.append('wii')
consoles.append('coleco')
consoles.append('gameboy')

# the general sorted() method will return a new sorted list of sorted items
# sort() will sort the list permanently
print(f"sort item temporarily: sorted(list): {sorted(consoles)}")
print(f"list after sorted {consoles}")
consoles.sort()
print(f"sort item permanently: list.sort(): {consoles}\n")

# reverse reverses the list by value
consoles.reverse()
print(f"print item in reversey: list.reverse(): {consoles}\n")

# for loop are similar to for each in java
print("for loop 'foreach': for item in item")
for console in consoles:
    print(f"\t {console}")

# python works with indentation, statements will belong to the parent indentation
# range() will return a range from start to stop
# print consoles using a for loop
print("\nfor loop 'classical': for i in range(start, stop)")
for i in range(0, len(consoles)):
    print(f"\t {consoles[i]}")

# range() thrid parameter will add a step to each number in range
print("\nlist of even numbers: range(start, stop, step")
even_numbers = list(range(2, 11, 2))
print(f"list of even numbers using list() and the range() method: \n{even_numbers}")

# manipulate each item in the range using a for loop
print(f"\nfirst 10 exponent:")
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(f"{squares}\n")

# list comprehension
print("creating list using list comprehension")
squares_comprehension = [value**2 for value in range(1, 11)]
print(f"list comprehension: list_name = [expression or method; for item; in iterable; if condition == True]")
print(f"squares using list comprehension: {squares_comprehension}\n")

# math methods
print("random math methods")
print(f"list.min(): {min(squares)}")
print(f"list.max(): {max(squares)}")
print(f"list.sum(): {sum(squares)}")

# list slice
print(f"\nConsoles: {consoles}")
sliced_consoles = consoles[0:3]
print(f"slice list: list[start:end]: {sliced_consoles}")
sliced_consoles2 = consoles[:4]
print(f"slice list from start: list[:end]: {sliced_consoles2}")
sliced_consoles3 = consoles[3:]
print(f"slice list until end: list[start:]: {sliced_consoles3}")

# list copy
# [:] required or else will only copy the reference and modify the same instance
consoles_copy = consoles[:]
consoles_copy.append("genesis")
print(f"\nlist copy: list[:]")
print(f"list copy + new item: {consoles_copy}")
print(f"original list: {consoles}")

# tuple: uses (), items are ordered, unchangeable, and allow duplicate values.
print("\ntuple: an immutable list: uses () instead of []")
games = ("final fantasy", "zelda", "chrono trigger")
print(games)
print(f"my favorite is {games[2]}")

print("the only way to modify a tuple is to reassign values to the variable")
games = ("final fantasy 3", "zelda: alttp", "chrono cross")
print(games)
