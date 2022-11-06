active = True
persons = []  # empty list

while active:
    name = input("enter name : ")
    age = input("enter age: ")
    age = int(age)  # cast string to int

    if age > 18:
        status = 'adult'
    else:
        status = 'kid'

    person = {}  # instantiate new person dictionary
    person['name'] = name
    person['age'] = age
    person['status'] = status

    persons.append(person)  # append person dictionary to list

    new_person = input(f"\nenter a new person? : ")
    if new_person == 'no':
        active = False

print("\nPerson List")
for person in persons:
    print(
        f"name = {person['name']} age = {person['age']} status = {person['status']}")
