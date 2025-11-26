# This program is to manage student enrollment using tuples.

# list of students as tuples
info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English")
]

# unique courses
unique_courses = set()

for tup in info:
    unique_courses.add(tup[1])

print(unique_courses)

# students enrolled in English
for name, course in info:
    if course == "English":
        print(f"Student enrolled in English: {name}")

# dictionary (students, set of courses)
dict = {}

for name, course in info:
    if (dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict)