consoles = ["playstation", "playstation 2", "playstation 3",
            "nintendo 64", "super nintendo", "gameboy color", "gameboy advance"]

print("check is consoles are playstations")
for console in consoles:
    if console.find("playstation") >= 0:
        print(console.title())
    else:
        print(f"{console}: this console is not a playstation")

print("\nlogical operators")
playstation_count = 0
nintendo_count = 0
other_count = 0

# else if is elif
for console in consoles:
    if console.find("playstation") >= 0:
        playstation_count += 1
    elif console.find("nintendo") >= 0:
        nintendo_count += 1
    else:
        other_count += 1

# python logical operators are: and, or, not
if playstation_count >= 2 and nintendo_count >= 2:
    print("i have too much stuff")

print("\ncheck stuff in 2 lists")
print(consoles)
wanted_consoles = ["playstation 2", "nintendo wii"]
for console in wanted_consoles:
    if console in consoles:
        print(f"i already have this console {console}")
    else:
        print(f"i have to buy a {console}")

# python identity operators are: is, is not
name = "booboo"
last = "bobo"
age = 16

if type(name) is not type(age):
    print(f"\nname type: {type(name)} age type {type(age)}")
    print("name and age are not the same type")
if type(name) is type(last):
    print(f"\nname type: {type(name)} last type {type(last)}")
    print("name and last name are the same type")
