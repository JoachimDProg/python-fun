# string and string formatting
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

# int and number string parsing
print("int and number string parsing")
add = 2+3
intstr = "23"
flotant = 2.345

print(add)
print(type(flotant))
print(type(add))
print("jai " + str(add) + " ans")
print(f"jai {str(add)} ans")

total = add + int(intstr)
print(total)
print("\n")

# array and loop
print("array and loop")
numarray = [1, 2, 3, 4, 5]
for n in numarray:
    print(n)
