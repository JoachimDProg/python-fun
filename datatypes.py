# in python, there is no need to implicitely write the data type
# it is possible to set a specific type: variable = type(value)
# numeric, strings and tuple are immutable
# list, dictionary and sets are mutable

# string and different string formatting
msg = "les chums"
name = "bobby"
last = "boucher"

# f-string
phrase = f"Hello {msg}, je m'apelle {name} {last}"

# format string
phrase2 = "Hello {}, je m'apelle {} {}".format(msg, name, last)

# % formatting
phrase3 = "Hello %s, je m'apelle %s %s" % (msg, name, last)

# whitespace string
whitespace = "   je suis vide             "

print("string and string formatting")
print(phrase)
print(phrase2)
print(phrase3)
print(whitespace.strip())
print("\n")

# numerical and numericals string parsing
print("numerical and numericals string parsing")
add = 2+3
intstr = "23"
flotant = 2.345

# verify types with type()
print(add)
print(type(flotant))
print(type(add))
print("jai " + str(add) + " ans")
print(f"jai {str(add)} ans")

total = add + int(intstr)
print(total)
print("\n")

# list and loop
print("list and loop")
numarray = [1, 2, 3, 4, 5]
for n in numarray:
    print(n)
