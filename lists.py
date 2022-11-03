#list
consoles = ["ps1", "ps2", "n64", "gameboy"]
print(f"print list: {consoles}")
print(f"print last item: list[-1]: {consoles[-1]}\n")

consoles.append('switch')
print(f"add element: list.append('element'): {consoles}\n")

consoles.insert(2, 'ps3')
print(f"insert element: list.insert(pos, 'element':): {consoles}\n")

del consoles[4]
print(f"delete element: del list[pos]: {consoles}\n")

#can pop by index, default is last
#python uses underscore for variables naming instead of camel casing
popped_console = consoles.pop(4)
print(f"pop element: list.pop(pos): {popped_console}\n")

consoles.remove("n64")
print(f"remove element: list.remote('value'): {consoles}\n")

consoles.append('switch')
consoles.append('wii')
consoles.append('coleco')
consoles.append('gameboy')
print(f"sort element temporarily: sorted(list): {sorted(consoles)}")
print(f"list after sorted {consoles}")
consoles.sort()
print(f"sort element permanently: list.sort(): {consoles}\n")

consoles.reverse()
print(f"print element in reversey: list.reverse(): {consoles}\n")

#for loop are similar to for each in java
print("for loop 'foreach': for item in item")
for console in consoles:
    print(f"\t {console}")

#python works with indentation, statements will belong to the parent indentation
print("\nfor loop 'classical': for i in range(start, end)")
for i in range(0, len(consoles)):
    print(f"\t {consoles[i]}")

print("\nmaking numerical lists")
#range 3rd param is step
even_numbers = list(range(2, 11, 2))
print(f"list of even numbers using a list and the range method: \n{even_numbers}\n")

print(f"first 10 exponent:")
squares = []
for value in range(1, 11):
    squares.append(value**2)
    
print(f"{squares}\n")

print("creating list using list comprehension")
squares_comprehension = [value**2 for value in range(1,11)]
print(f"list comprehension: list_name = [expression or method for value in range(start, stop)]")
print(f"squares using list comprehension: {squares_comprehension}\n")

print("random math methods")
print(f"list.min(): {min(squares)}")
print(f"list.max(): {max(squares)}")
print(f"list.sum(): {sum(squares)}")
    